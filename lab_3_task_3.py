from  fis_const import *
from math import sin, cos, tan, pi
import numpy as np
a = 30*(pi/180)
x0 = 0
y0 = 0
U0 = 15
t = np.linspace(0, 5, 100)

U0x = U0*(cos(a))
U0y = U0*(sin(a))

x = x0 + U0x*t
y = y0 + U0y*t - (g*(t**2)*(1/2))

A = np.ndarray(shape=(100, 3))
for i in range (100):
  A[i,0] = t[i]
  A[i,1] = x[i]
  A[i,2] = y[i]
print(A)