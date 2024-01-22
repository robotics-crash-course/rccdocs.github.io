# Python Functions and Classes

The first rule of programming is don't repeat yourself, the second rule is don't repeat yourself! 

## Writing Functions
Functions are essential to following the aforementioned rules of programming. Functions allow us to execute the same line(s) of code over and over, and the best part is, if we do it right, we only have to type those lines once! 

While not necessarily required, most functions take `inputs` and `return` something.  

In Python: first define the name of the function, the number of inputs, the code that is executed, and then what the function returns. 

```python
def add(a, b):
    return a + b

def exp(b, p):
    return b ** p

def area(r):
    return 3.14 * r**2
```
Once they are defined (upload functions to the pico by running the script that contains the function definitions), we can `call` the functions like this:
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

## Classes
In Python, most if not all `functions` are `members` of `classes`. 

`Classes` store groups of information that is related. Classes can contain variables and functions. Anything that the class contains is called a `member` of that class. Let's look at an example class, the class written to store all of the functions related to hardware on the Raft Board. (The full class is defined in `micropython/include/rcc_library.py`)

```python
class Raft:
    def led_on(self):
        #turn on LED
    def led_off(self):
        #turn off LED
```

Inside this example `class`, there are two `member functions`, and they either turn on or off the led on the Pico. 

##### Pro-Tip: the `self` parameter means that the function takes in all of the other members (all the information) within the class. 

## Using Classes in our Scripts
There are a few steps to use any class within MicroPython. 

First, must import the `module` into the script. The module is the python script containing any number of classes that you want to use. 

```python
from include.rcc_library import Raft
```
This line means from the python file within the include folder called rcc_library import the Raft class to this script. 

Second, `instantiate` or make an `instance` of the class. You can name these whatever you'd want, but for ease of debugging our scripts in this course, will typically use my...something to name our classes. 

```python
myraft = Raft()
```
Need the parenthesis to indicate we want to execute/create an instance of the Raft class, naming it myraft. 

To call functions that are members of classes, use the `.` or `dot-operator`.

```
myraft.led_on()
```
Once again, need to use parenthesis to run the function. 



## Using Raft Class to Turn on LED

Make a new script within your scripts folder, let's explore the Raft class:

```python
#this script turns on the Pico's LED

#import the class 
from include.rcc_library import Raft

#make instance of the class
myraft = Raft()

#call the led_on function
myraft.led_on()
```
When you first run this script, you'll most likely see this error: 

`ImportError: no module named 'include'`

This is because the pico does NOT have all of the RCC-written modules and classes preinstalled, why would it? 

To upload all the modules to the Pico, use the MicroPico commands:

First, use `CTRL+Shift+P` to open the commands, then search for `MicroPico: Upload Project to Pico`. Use this command to upload all of the modules. 

Now, when you run the script, the green led should turn on! 

## Using utime 
utime is a module already imported within MicroPython. There are several functions within this class that are all related to time when the code is running. 

The easiest one to use is `sleep_ms()`. This function takes the time in milliseconds (1/1000 seconds). While this function is running, nothing will happen on the pico. 

If we wanted to turn on the LED for one second, our script would look like this:

```python
from include.rcc_library import Raft
import utime

myraft = Raft()
myraft.led_on()
utime.sleep_ms(1000) 
myraft.led_off()
```

## Using Conditionals/Logic to Play with LED

`if` we only want the LED to be on at certain times, we can use if-statements to do that! 

```python
from include.rcc_library import Raft

myraft = Raft()

favcolor = "blue"
age = 24

if favcolor == "blue" and age > 13:
    myraft.led_on()
```

When this script is run, the if-statement checks if the variable `favcolor` is equal to a string `blue`, `and` if the variable age is greater than 13. If both are `True`, then the `led_on()` function will run, turning on the LED. 

## Summary
In this guide, we learned how to write functions in python, how to navigate classes, and how to use the rcc_library to turn on the Pico's LED!