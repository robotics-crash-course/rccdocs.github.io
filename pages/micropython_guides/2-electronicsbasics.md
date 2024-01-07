# Connecting our Code to the Physical World

#### What is a Pico anyway?!?

A microcontroller, in our case the Raspberry Pi Pico, is the brain of our robot. The Pico runs our python scripts but it can also be programmed with C or C++. 

The Pico interacts with all of the different components on the robot, it can generate and read voltages for both analog and digital devices. 

#### woah woah slow down... what does voltage, analog, and digital mean??

## Understanding Voltage
Planning on going over essentials of these topics in lecture, the lecture is based on Sparkfun's guides and videos:

+ [Sparkfun's guide to Voltage and Electricity](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/all)

+ [Sparkfun's guide to Analog vs Digital](https://learn.sparkfun.com/tutorials/analog-vs-digital)


## The Raft
The Raft is the PCB (Printed Circuit Board) that allows us to connect the Pico to all of the devices on our robots. You can read more about the nitty-gritty of the Raft [on the datasheet](https://github.com/robotics-crash-course/rccdocs.github.io/blob/main/pages/html_pages/RAFT-DATASHEET.pdf)


## Connecting to our Code
The Pico interacts with the physical world through its GPIO Pins (General Purpose Input Output). 

The Pico is a 3.3V logic device, meaning if we connect +3.3V to an `Input` GPIO Pin, the `value` of that pin will be `1`. 

If we use a GPIO pin as an `Output` Pin, and we give a `value` a value of `1` to that pin, that pin will have +3.3V of potential to connect to any other device on our robot. 

There are 3 special pins on the Pico that can be used to read `Analog` voltages. These pins are connected to a ADC (or analog to digital converter), and we can read the value as a number ranging from 0-65536 which corresponds linearly to 0-3.3V. (More on analog devices later, let's understand digital first)

## First Output Pin: the LED on the Pico
There are 3 lines of Python required to turn on the LED that's onboard the Pico:

```python
from machine import Pin

led = Pin("LED", Pin.OUT)

led.value(1)
```
Create a new file within the scripts folder inside VS Code, add these 3 lines, and run the script! You should see the green LED turn on!

There is a lot of Python to unpack with those 3 short lines, but we'll get there;)

## Let's Setup 2 Pins: Output and Input 
Create another file within the scripts folder in VS Code, and enter these lines:

```python
from machine import Pin

outputpin = Pin(0, Pin.OUT)
outputpin.value(1)

inputpin = Pin(4, Pin.IN)

while True:
    print(inputpin.value())
```
Run this file, what does the REPL say? Grab a jumper wire and connect Pin 0 and Pin 4 (the green pins on the Raft). How does the output of the REPL change once the pins are connected? Try connecting other GPIO pins to Pin 4, does anything happen?


## Summary
There is a lot of information packed into this lesson, before we move on to explaining the Python code its important to understand the following:

+ The Pico connects to the physical world by creating and reading voltage levels
+ We can use GPIO pins as inputs to read voltage levels, 3.3V equals a digital value of 1
+ We can use GPIO pins as outputs to generate 3.3V to power and communicate with devices connected to the Pico