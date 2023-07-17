import matplotlib
import matplotlib.pyplot as plt
import numpy as np

tau_min = 0
tau_max = 10
dt = 0.1

t = np.arange(tau_min, tau_max, dt)
x = 3*t**2 + 5*t + 7
velArr = []
i = tau_min + dt
j = 0

while (i < tau_max):
    x1 = 3*(tau_min+j*dt)**2 + 5*(tau_min+j*dt) + 7
    x2 = 3*(tau_min+(j+1)*dt)**2 + 5*(tau_min+(j+1)*dt) + 7
    curVel = (x2-x1)/dt
    print(curVel)
    velArr.append(curVel)
    i+=dt
    j+=1

fig, ax = plt.subplots()
ax.plot(t, x, 'b', label = 'distance function')
ax.plot(t, velArr, 'r', label = 'velocity function')
ax.set(xlabel= 'time', ylabel= 'distance/velocity', title= 'Differentiation Side Quest')
ax.legend(loc = 'upper right')
ax.grid()
plt.show()