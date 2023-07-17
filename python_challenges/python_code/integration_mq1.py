import matplotlib
import matplotlib.pyplot as plt
import numpy as np

time1 = 0
time2 = 3
delt = 0.000001

def integrate(tau1, tau2, dt):
    i = 1
    j = tau1
    totalArea = 0
    while (j+dt < tau2):
        h = 6*(tau1+i*dt) + 5
        b = dt
        area = h*b
        totalArea+=area
        i+=1
        j+=dt
    return totalArea

currDist = integrate(time1, time2, delt)
print(currDist)
