from scipy import interpolate
import numpy as np
xnew = np.linspace(1.0,13.0,500)
x = np.linspace(1.0, 13.0, 7)
y = np.sin(x)
ynewLinear = interpolate.spline(x,y,xnew,order = 1)