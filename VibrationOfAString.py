# Author - kalais
# Vibration of a string with damping using matplotlib for animation
# CFL criterion is used for stability of the solution, which uses
#               finite differences for PDE solving
# REQUIRES - MATPLOTLIB module for animation
# Vibrating string length 1 unit, deltaX is 0.01 unit. Time step - held constant at 0.001 seconds.
# For animation without damping, dampCoefficient should be set to 0.0

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

deltaT, deltaL = 0.001, 0.01
extent, uold, deltaX = [], [], 0.0
for i in range(41):
    uold.append((i/40)*0.25)
    if len(extent) == 0:
        extent.append(i)
        deltaX = 0.01
    else:
        extent.append(extent[len(extent)-1]+deltaX)

for i in range(1,60):
    uold.append(((59.6/60)-(i/60))*0.25)
    extent.append(extent[len(extent)-1]+deltaX)
uold.append(0.0)
extent.append(1.0)

unow, unext, dampCoefficient = uold[:], [], 0.0005

for i in range(10000000):
    unext = [0 for j in range(len(unow))]
    unext[0]=unow[0]
    unext[-1]=unow[-1]
    for k in range(1, len(unow)-1): # --> Actual solving happens here. This solves for string position at a time instant, once the string is released.
        unext[k] = (2*unow[k]-(uold[k]*(1-(dampCoefficient/2))) + (unow[k-1]-(2*unow[k])+unow[k+1])*((deltaT/deltaL)**2))/(1 + (dampCoefficient/2))

    uold = unow[:]
    unow = unext[:]
    unext = []
    if(i%50 == 0): # clear the current figure and replot
        plt.clf()        
        plt.plot(extent, unow)
        plt.xlim(-0.1, 1.1)
        plt.ylim(-1.0, 1.0)
        plt.pause(0.001)
plt.show()
