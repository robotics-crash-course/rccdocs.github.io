import matplotlib
import matplotlib.pyplot as plt
import numpy as np

time1 = 0
time2 = 3
delt = 0.000001
distArr = []

def integrate(tau1, tau2, dt):
    i = 1
    j = tau1
    totalArea = 0
    while (j < tau2):
        h = 6*(tau1+i*dt) + 5
        b = dt
        area = h*b
        totalArea+=area
        distArr.append(totalArea)
        i+=1
        j+=dt
    return totalArea

currDist = integrate(time1, time2, delt)
print(currDist)

t = np.arange(time1, time2, delt)
v = 6*t + 5

fig, ax = plt.subplots()
ax.plot(t, v, 'b', label = 'velocity function')
ax.plot(t, distArr, 'r', label = 'distance function')
ax.set(xlabel= 'time', ylabel= 'distance/velocity', title= 'Integration Side Quest')
ax.legend(loc = 'upper right')
ax.grid()
plt.show()