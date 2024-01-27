# Drive Control Library

This library can be found within the [micropython repository](https://github.com/robotics-crash-course/micropython) (See this repository more detail on the helper functions)

The Drive Control library uses the wheel odometry and IMU (inertial measurement unit) on the robot to set motor power on the wheels. 

The Drive Controller operates based on 2 desired inputs: 
1. wheel velocity
2. orientation of robot

Using the drive controller allows you to update the desired wheel velocity and the desired orientation that the robot faces or drives at. Using the controller requires setting up the `controller class` and calling the `start()` function. 

## Controller Setup

```python
from util.drivecontrol import Controller

mycontroller = Controller()

mycontroller.start()
```
## Available Helper Functions (to call within algorithms or state machines)

```python
from util.drivecontrol import Controller

mycontroller = Controller()

# drive forwards
mycontroller.drive_forwards()

#drive backwards
mycontroller.drive_backwards()

#stop both motors
mycontroller.stop()

#updates desired angle += 90 degrees
mycontroller.left_turn()

#updates desired angle -= 90 degrees
mycontroller.right_turn()

#updates desired angle += 180 degrees
mycontroller.u_turn()

#updates desired angle += 30 degrees
mycontroller.custom_left_turn(30) 

#updates desired angle -= 30 degrees
mycontroller.custom_right_turn(30)
```

## Using Odometry Counts 
Since the counts are now stored within the controller class, use the following syntax to find the value of each wheel's count:

```python
from util.drivecontrol import Controller

mycontroller = Controller()

mycontroller.start()

while True:
    print(mycontroller.left_odom.get_count(), mycontroller.right_odom.get_count())
```

## Using Lidar 
Since the Raft's i2c bus is stored within the controller class, use the following to get distances from the lidar sensor:

```python
from util.drivecontrol import Controller
from sensors.vl53l0x import VL53L0X

mycontroller = Controller()
mycontroller.start()

mylidar = VL53L0X(mycontroller.raft.i2c_bus)

while True:
    print(mylidar.get_distance())
```