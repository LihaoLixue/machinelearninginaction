#!/usr/bin/python
# coding=utf-8

import urllib2, json, commands, time, datetime, logging
# import configparser
from ConfigParser import ConfigParser

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='generate_successV1.log',
                    filemode='a')

CONFFILE = "topic.ini"
INTERVAL = 100
COUNT = 36
RETRY = 3

topic_path_list = {}
topic_url_list = {}
topic_logsize = {}

def init_topic_info():
    config = ConfigParser()
    config.read(CONFFILE)
    sec = config.sections()
    for topic in sec:
        kmon = config.get(topic, "kmon")
        group = config.get(topic, "group")
        zkconnect = config.get(topic, "zkconnect")
        path = config.get(topic, "path")
        url = kmon + "?" + "topic=" + topic + "&group_id=" + group + "&zk_connect=" + zkconnect
        topic_url_list[topic] = url
        topic_path_list[topic] = path

def get_url_json(topic, url):
    try:
        topic_json = urllib2.urlopen(url).read()
    except Exception as e:
        logging.error("topic " + topic + " error " + str(e))
        topic_json = None
    return topic_json

def retry_get_json(topic, url):
    try_cnt = 0
    topic_json = get_url_json(topic, url)
    while try_cnt < RETRY:
        if topic_json is None:
            topic_json = get_url_json(topic, url)
            try_cnt += 1
            time.sleep(3)
        else:
            try_cnt = 0
            break
    return (try_cnt, topic_json)

def init_logsize():
    for topic, url in topic_url_list.items():
        try_cnt, topic_json = retry_get_json(topic, url)
        if try_cnt > 2:
            logging.error("fail to get topic " + topic + " logsize info!")
            continue
        topic_load = json.loads(topic_json)
        topic_partition = {}
        if not len(topic_load):
            logging.warning("topic " + topic + " no partition ")
            continue
        for tl in topic_load:
            topic_partition[tl["partition"]] = tl["logSize"]
        topic_logsize[topic] = topic_partition

def generate_success(path):
    dpath = datetime.datetime.now() + datetime.timedelta(days=-1)
    success_file = path + "/" + dpath.strftime('%Y%m%d') + "/_SUCCESS"
    err, out = commands.getstatusoutput("/home/bigdata/software/hadoop/bin/hdfs dfs -touchz " + success_file)
    if err:
        logging.warning("generate file " + success_file + " failed!!!  error: " + out)
    else:
        logging.info("generate file " + success_file + " success!!!")
        out = commands.getstatusoutput("/home/bigdata/software/hadoop/bin/hdfs dfs -chown bi:bi " + success_file)
    return err

def check_tmpfile(path):
    dpath = datetime.datetime.now() + datetime.timedelta(days=-1)
    tmpfile = path + "/" + dpath.strftime('%Y%m%d')
    res = commands.getoutput("/home/bigdata/software/hadoop/bin/hdfs dfs -ls -R" + tmpfile + "| grep '.tmp' |wc -l")
    return int(res.split()[-1])

def roll_tmpfile(path):
    print("print roll_tmpfile")
    dpath = datetime.datetime.now() + datetime.timedelta(days=-1)
    tmpfile = path + "/" + dpath.strftime('%Y%m%d')
    res = commands.getoutput("/home/bigdata/software/hadoop/bin/hdfs dfs -ls -R " + tmpfile + "| grep '.tmp' | awk '{print $NF}'")
    path_list = res.split("\n")
    print(path_list)
    now_hour = int(datetime.datetime.now().strftime("%H"))
    for p in path_list:
        dst = p.replace("/.", "/").replace(".tmp", "")
        err, out = commands.getstatusoutput("/home/bigdata/software/hadoop/bin/hdfs dfs -ls " + p +"| awk '{print $6,$7}'")
        if err:
            logging.warning(" get temp file time " + p + " failed!!! ")
            continue
        try:
            hour = out.split()[1].split(":")[0]
        except IndexError:
            logging.warning(" fetch file time is error!!! " + out)
            continue
        if (int(hour) < 23 and now_hour == 0) or now_hour == 1:
            err, out = commands.getstatusoutput("/home/bigdata/software/hadoop/bin/hdfs dfs -mv " + p + " " + dst)
        if err:
            logging.warning("roll tmp file " + path + " failed!!!  error: " + out)
            return err
    return 0

def main():
    i = 1
    roll_once = True
    init_topic_info()
    init_logsize()
    while True:
        if len(topic_logsize) == 0:
            logging.info("topic all done")
            return
        time.sleep(INTERVAL)
        i += 1
        for topic, logsizedic in topic_logsize.items():
            if check_tmpfile(topic_path_list[topic]):
                logging.warning("topic " + topic + " has tmp file")
                if roll_once:
                    if not roll_tmpfile(topic_path_list[topic]):
                        logging.warning("tmp file " + topic_path_list[topic] + " has be force rolled!")
                if int(datetime.datetime.now().strftime("%H")):
                    if not roll_tmpfile(topic_path_list[topic]):
                        logging.warning("tmp file " + topic_path_list[topic] + " has be force rolled!")
                continue
            url = topic_url_list[topic]
            #todo ：whether is necessary
            try_cnt, topic_json = retry_get_json(topic, url)
            if try_cnt > 2:
                logging.error("fail to get topic " + topic + " offset info!")
                continue
            topic_load = json.loads(topic_json)
            generate = True
            for tl in topic_load:
                partition = tl["partition"]
                logsize = logsizedic[partition]
                offset = tl["offset"]
                #todo 当一个业务量十分大，lag一直不为0时，此时永远生成不了success文件
                if offset < logsize:
                    logging.warning("topic " + topic + " partion " + str(partition) + " offset:" + str(offset) + " less than logsize:" + str(logsize))
                    generate = False
                    break
            if generate:
                err = generate_success(topic_path_list[topic])
                if not err:
                    del topic_logsize[topic]
        if i > COUNT:
            logging.warning("topic check time out")
            break
        roll_once = False

if __name__ == "__main__":
    main()
