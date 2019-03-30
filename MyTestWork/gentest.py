import threading
import urllib.request as urllib2, json, subprocess as commands, time, datetime, logging

dict = {'a': 1, 'b': 2, 'c': '3', 'd': '3', 'e': '3', 'f': '3', 'g': '3', 'h': '3', 'i': '3'}
# dict = {'a': 1, 'b': 2, 'c': '3'}
lista = []
listb = []


def getFetch(func, num):
    if len(func) % num == 0:
        spl = len(func) // num
    else:
        spl = len(func) // num + 1
    for i in range(num):
        listb.append(func[0:spl])
        del (lista[0:spl])
    print(listb)


def getFetcher(topic_logsize):
    for key in topic_logsize.keys():
        lista.append(key)
    if len(lista) >= 0:
        numThread = len(lista) // 2 + 1
        if numThread > 1:
            getFetch(lista, numThread)
        else:
            getFetch(lista, 1)


def run(list):
    i = 1
    while True:
        if len(list) == 0:
            logging.info("topic all done")
            return
        i += 1
        for topic in list:
            if check_tmpfile(topic_path_list[topic]):
                logging.warning("topic " + topic + " has tmp file")
                if roll_once:
                    if not roll_tmpfile(topic_path_list[topic]):
                        logging.warning("tmp file " + topic_path_list[topic] + " has be force rolled!")
                if int(datetime.datetime.now().strftime("%H")):
                    if not roll_tmpfile(topic_path_list[topic]):
                        logging.warning("tmp file " + topic_path_list[topic] + " has be force rolled!")
                continue
            err = generate_success(topic_path_list[topic])
            if not err:
                del topic_logsize[topic]
        if i > COUNT:
            logging.warning("topic check time out")
            break
        roll_once = False


threads = []
files = range(len(listb))
for i in files:
    t = threading.Thread(target=run(), args=(list[i],))
    threads.append(t)
if __name__ == '__main__':
    for i in files:
        threads[i].start()
for i in files:
    threads[i].join()













for key in dict.keys():
    lista.append(key)
if len(lista) >= 0:
    numThread = len(lista) // 2 + 1
    if numThread > 1:
        getFetch(lista, numThread)
    else:
        getFetch(lista, 1)

threads = []
files = range(len(listb))
for i in files:
    t = threading.Thread(target=player, args=(list[i],))
    threads.append(t)
