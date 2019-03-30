from Ch05 import LR_demo
import numpy as np

mat, label = LR_demo.loadDataSet()
# weights, weights_history = LR_demo.gradAscent(mat, label)
weights = LR_demo.stocGradAscent0(np.array(mat), np.array(label))
print(weights)
# LR_demo.plotBestFit(weights)
# LR_demo.plot_weights_update(weights_history)
