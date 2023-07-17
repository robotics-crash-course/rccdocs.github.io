import matplotlib
import matplotlib.pyplot as plt
import numpy as np

tau = 0
dt = 0.0001
end_time = 3

t = np.arange(-5, 5, dt)
x = 3*t**2 + 5*t + 7

fig, ax = plt.subplots()
ax.plot(t, x, label = 'Original Function')
ax.set(xlabel= 'Time (s)', ylabel= 'Distance (m)')
ax.legend(loc = 'upper right')
ax.grid()
plt.show()