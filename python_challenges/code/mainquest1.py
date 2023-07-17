import matplotlib
import matplotlib.pyplot as plt
import numpy as np

i = 0
tau = 0
dt = 0.0001
arr = []
vel = 0
end_time = 3

t = np.arange(tau, end_time, dt)
x = 3*t**2 + 5*t + 7

#Main Quest
curr_dist = tau**3 + 3*tau**2 + 5*tau + 7
next_dist = (tau+dt)**3 + 3*(tau+dt)**2 + 5*(tau+dt) + 7
vel = (next_dist - curr_dist)/dt
print(vel)