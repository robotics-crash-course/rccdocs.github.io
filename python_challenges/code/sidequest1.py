import matplotlib
import matplotlib.pyplot as plt
import numpy as np

i = 0
tau = 0
dt = 0.001
arr = []
vel = 0
end_time = 3

t = np.arange(tau, end_time, dt)
x = 3*t**2 + 5*t + 7


while (i < end_time/dt):
    curr_dist = 3*(tau+i*dt)**2 + 5*(tau+i*dt) + 7
    next_dist = 3*(tau+(i+1)*dt)**2 + 5*(tau+(i+1)*dt) + 7
    vel = (next_dist - curr_dist)/dt
    arr.append(vel)
    i+=1

fig, ax = plt.subplots()
ax.plot(t, x, label = 'Original Function')
ax.plot(t, arr, label = 'Derivative Function')
ax.set(xlabel= 'Time (s)', ylabel= 'Distance (m)')
ax.legend(loc = 'upper right')
ax.grid()
plt.show()