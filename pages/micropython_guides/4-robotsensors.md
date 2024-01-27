# Using Robot's Raw Components

In this guide, will provide syntax for the helper functions within the [micropython repository](https://github.com/robotics-crash-course/micropython) (See this repository more detail on the helper functions)

To see the pinout for the default pins used in the libraries, see [Raft v0.6 Pinout](https://robotics-crash-course.github.io/rccdocs.github.io/pages/html_pages/newpinout.html)

## Raft Setup and Helper Functions

```python
from include.rcc_library import Raft

myraft = Raft()

myraft.led_on()
myraft.led_off() 

myraft.setup_button() #adds pull-down resistor
myraft.setup_button_counter() 

while True:
    print(myraft.get_button(), myraft.button_counter())
```

## Motor Power

```python
from include.pwm_helper import Motors

mymotors = Motors()
mymotors.setup()

while True:
   mymotors.set_power(40,40) #left wheel, right wheel
```

## Wheel Odometry 
```python
from include.rcc_pins import Pins
from sensors.odom import Directional_Odom

# left wheel
myleftodom = Directional_Odom()
myleftodom.setup(Pins.LEFT_DIR, Pins.LEFT_INT)

# right wheel
myrightodom = Directional_Odom()
myrightodom.setup(Pins.RIGHT_DIR, Pins.RIGHT_INT)

while True:
    print(myleftodom.get_count(), myrightodom.get_count())

```
## IMU (Inertial Measurement Unit)

```python
from include.rcc_library import Raft
from sensors.mpu6050 import MPU6050

myraft = Raft()
myraft.setup_i2c()

myimu = MPU6050(myraft.i2c_bus)

while True:
    print(myimu.get_angvel_z()) #angular velocity around z-axis
```
## Lidar 

```python
from include.rcc_library import Raft
from sensors.vl53l0x import VL53L0X

myraft = Raft()
myraft.setup_i2c()

mylidar = VL53L0X(myraft.i2c_bus)

while True: 
    print(mylidar.get_distance()) #millimeters
```
