# Python Functions and Classes

The first rule of programming is don't repeat yourself, the second rule is don't repeat yourself! 

## Writing Functions
Functions are essential to following the aforementioned rules of programming. Functions allow is us to execute the same line(s) of code over and over, and the best part is, if we do it right, we only have to type those lines once! 

While not necessarily required, most functions take inputs and return something.  

In Python: first define the name of the function, the number of inputs, the code that is executed, and then what the function returns. 

```python
def add(a, b):
    return a + b

def exp(b, p):
    return b ** p

def area(r):
    return 3.14 * r**2
```
Once they are defined, we can `call` the functions like this:
```python
x = 2
y = 6

c = add(x,y)
# c = 8
d = exp(x,y)
# d = 64
a = area(y)
# a = 113.04
```
Fun Fact: If you run a script that defines functions, those functions are stored in the REPL and you can call them again and again with different inputs to see the value that is returned. 

## Getters and Setters
Typically, functions that are tailored for the Pico are either getters or setters. Getter functions return the value of a sensor reading or simply the value of a gpio pin. Setter functions set a motor speed or position, or simply set the value of a gpio pin. 

For GPIO pins, the `value()` function can be either a getter or a setter depending on if the gpio is setup as an input or output. 

As a `setter` function, `value()` takes either 0 or 1 as it's input, and it sets the desired voltage at the pin. 

As a `getter` function, `value()` returns either 0 or 1 based on the voltage found at the gpio pin. 

## Classes
There are 26 GPIO pins on the Pico. Since they all have the same basic functionality; they all can use the `value()` function. Since the value function is the same every time, but we want to be able to use that function for every Pin available on the Pico, the value function is stored inside a Python `Class`

The basic structure of the Pin class (and any class in Python) is as follows:

The `__init__()` function is run when the class is initialized or instantiated (an instance is created).

Anything defined in the class is called using the `.` operator. 

`self` is an input to all members functions of the class.  

```python
Class Pin:
    def __init__(self, number, direction):
        # sets up functionality
    def value(self, optional_output_value):
        # returns 0 or 1 if input
        # sets voltage at pin if output

#to call the function within the class, setup an instance of the class for each pin

#pin 0 as output
outputpin = Pin(0, Pin.OUT)
outputpin.value(1)

#pin 4 as input
inputpin = Pin(4, Pin.IN)
print(inputpin.value())
```

Since the class is not defined within our script, we need to import the class into our script, the Pin class is within the machine `module` which is why we use:

```python
from machine import Pin
```
## Another Example ~ Using RCC-Built Modules
The Pin class is one of the more complicated classes within the machine module. Another example of a class would be the class we wrote for the Raft. 

Make a new script within your scripts folder, let's explore the Raft class

```python
#import the class from the include folder
from include.rcc_library import Raft

#make your own instance of the class
myraft = Raft()

#call the led_on function
myraft.led_on()

```
When you run this script, you'll most likely see this error: 

`ImportError: no module named 'include'`

This is because the pico does NOT have all of the RCC-written modules and classes preinstalled, why would it? 

To upload the modules to the Pico, use the MicroPico commands:

First, use `CTRL+Shift+P` to open the commands, then search for `MicroPico: Upload Project to Pico`. Use this command to upload all of the modules. 

Now, when you run the script, the led should turn on! 

Let's take a deeper dive into the class: to see class's definition, click on the class within your script, and press `F12`. 

Within the `Raft()` class, we see the init function does not take any arguments but it sets up the led as an output pin!

```Python
class Raft:
    def __init__(self):
        self.led = Pin("LED", Pin.OUT)

    def led_on(self):
        self.led.value(1)
        return "LED ON"
```
There's nothing really that special going on in this class, just a renaming of the value() function that we're already familiar with.

See if you can figure out what the other LED-related functions are doing, call them in your script OR in the REPL! 

## Using the Button on the Raft
To use the button, there are a few functions within the Raft class you'll need. Make a new script within the scripts folder in VS code. 

```python
from include.rcc_library import Raft

myraft = Raft()

myraft.setup_button()
myraft.setup_button_counter()

while True:
    print(myraft.get_button(), myraft.button_counter())

```
Run this script and press the button on the Raft labeled *22. What is the difference between the result of `get_button()` and the `button_counter()`? 


## CHALLENGE: Combine everything we've learned so far! 

Create a new script within your scripts folder:

**Turn the LED ON only when the button is pressed.**




