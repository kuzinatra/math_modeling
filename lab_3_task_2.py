from  fis_const import *
from math import sin, cos, tan, pi
import numpy as np
H = 100
a = pi/3
B = 30*(pi/180)
U = ((g*H*(tan(B)**2))/(2*(cos(a)**2)*(1-(tan(B))*(tan(a)))))**0.5
print(U)

T = 200
E = 300
N = (2/pi**0.5)*(h/((k*T)**(3/2)))*(e**(-E/(k*T)))*(E**(T/2))
print(N)