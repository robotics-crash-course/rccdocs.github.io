# PID Control

The PID controller class calculates an output based on the error between a desired state and an actual state of the robot. For example, using a desired velocity of each wheel, or the desired angular velocity of the robot, or even the desired orientation the robot drives at. 

The `PID_Control` class is used in the following way, but when in doubt, just read the code ;)

## Instantiation

```python
from util.pidcontrol import PID_Control

mycontroller = PID_Control(kp, ki, kd, Ts, sigma, lowerLimit, upperLimit, errorDotEnabled=False, antiWindupEnabled=False)
```

Theres several values that go into the init function, each of which can also be setup with the following helper functions:

```python
mycontroller = PID_Control()

mycontroller.setGains(kp, ki, kd)
mycontroller.setTimeParameters(Ts, sigma) #Ts = 0.02 is 20 ms
mycontroller.setLimits(lowerLimit, upperLimit)
```

## Putting Controller in a Timer (for exact dt intervals)

Micropython has easily-implementable timers which you can put the controller and other sensors readings or motor commands as needed. *Make sure the period of the timer is the same value as the Ts in the PID Control class.*

```python
from machine import Timer

def controller_callback(timer):
    controller_output = mycontroller.pid(desired, actual)
    #do something wiht the controller output here~~

timer = Timer(mode=Timer.PERIODIC, period=20, callback=controller_callback) #20 ms
```

## Example for Angular Velocity
In this example, the desired angular velocity of the robot is 100 degrees per second and the control loop is running every 20 ms. You can and should be fancy and write the callback function within a class (such as the drive controller class), but for this example everything is within the one python file.


```python
from include.rcc_library import Raft
from sensors.mpu6050 import MPU6050
from util.pidcontrol import PID_Control
from include.pwm_helper import Motors
from machine import Timer

myraft = Raft()
myraft.setup_i2c()
myimu = MPU6050(myraft.i2c_bus)
mycontroller = PID_Control(1, 0, 0, 0.02, 0.05, -50, 50, False, False)
mymotors = Motors()
mymotors.setup()

desired_angular_velocity = 100
controller_output = 0

def controller_callback(timer):
    angular_velocity = myimu.get_angvel_z()
    controller_output = round(mycontroller.pid(desired_angular_velocity, angular_velocity))
    mymotors.set_power(-controller_output, controller_output)
    
timer = Timer(mode=Timer.PERIODIC, period=20, callback=controller_callback)

while True:
    print(desired_angular_velocity, controller_output)
```
