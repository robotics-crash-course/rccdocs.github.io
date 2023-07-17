import matplotlib
import matplotlib.pyplot as plt
import numpy as np

time = 0
delt = 0.5

def differentiate(tau, dt):
    x1 = 3*tau**2 + 5*tau + 7
    x2 = 3*(tau+dt)**2 + 5*(tau+dt) + 7
    vel = (x2-x1)/dt
    return vel

currVel = differentiate(time, delt)
print(currVel)