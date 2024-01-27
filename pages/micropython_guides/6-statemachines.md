# State Machines 

The drive controller class is very helpful in taking care of the robot's velocity and orientation in the background (it is running on the second core of the Pico), so that in the main core (in our script), we can focus on our algorithm or state machine. 

`State Machines` are an incredibly helpful tool in building algorithms for mobile robots and robotics in general. 

To use them with the [micropython repository](https://github.com/robotics-crash-course/micropython)'s drive controller class, each `state` of the robot/algorithm gives one command to the drive controller. 

The `transition conditions` between the states can be either the odometry counts, the lidar, or simply using timing/sleep functions. (Because controller is running in second thread, sleep functions are non-blocking). 

## 3 State Machine Examples
In this example, the robot drives forwards and backwards certain distances based on the odometry. 

```python
from util.drivecontrol import Controller
mycontroller = Controller()
mycontroller.start()

state = 0

while True:
    # Forwards State
    if state == 0:
        mycontroller.drive_forwards()

        # Odometry Based Transition Condition
        if mycontroller.left_odom.get_count() >= 1500 and mycontroller.right_odom.get_count() >= 1500:
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()
    
    # Backwards State
    if state == 1:
        mycontroller.drive_backwards()

        # Odometry Based Transition Condition
        if mycontroller.left_odom.get_count() <= -1500 and mycontroller.right_odom.get_count() <= -1500:
            state = 0
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()
```

In this second example, the robot drives in a square shape, turning after 1500 counts on each wheel. 

```python
from util.drivecontrol import Controller
mycontroller = Controller()
mycontroller.start()

state = 0 #setup initial state

while True:
    #Forwards State
    if state == 0:
        mycontroller.drive_forwards()

        # Odometry Based Transition Condition
        if mycontroller.left_odom.get_count() >= 1500 and mycontroller.right_odom.get_count() >= 1500:
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()

    #Turning State
    elif state == 1:
        mycontroller.left_turn()
        state = 0
```

In this third example, the robot will stop after completing a square driving pattern: 

```python
from util.drivecontrol import Controller
mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0

while True:
    # Forwards State
    if state == 0:
        mycontroller.drive_forwards()

        # Odometry Based Transition Condition
        if mycontroller.left_odom.get_count() >= 1500 and mycontroller.right_odom.get_count() >= 1500:
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()

    # Turning State
    elif state == 1:
        mycontroller.left_turn()
        turns_made += 1

        #Two Option Transition Condition
        if turns_made > 4:
            state = 2
        else:
            state = 0

    #Stop State
    elif state == 2:
        mycontroller.raft.led_on()
        mycontroller.stop()

        #No Transition Conditions
```



