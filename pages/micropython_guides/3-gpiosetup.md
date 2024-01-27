# Using Pin Class to Setup GPIO Pins

In this guide, we will use micropython to setup GPIO pins as inputs and outputs, write and read the values of the pins, and add resistors to give inputs a default state. 

For reference: [Pico W Datasheet](https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf)

## Output Pin Setup

Output pins are able to generate digital signals, they can either have `0V` or `3.3V`, the logic voltage level for the Pico microcontroller. 

To setup any of the GPIO (General Purpose Input Output) pins as an `output` pin, use the following lines: 

In this example, using pin `3` as an output pin. 

```python
from machine import Pin

output_pin = Pin(3, Pin.OUT)
```

## Using Output Pin
To `write` or `put` logic-high or 3.3V on the output gpio pin, use the `value()` function where the input to the function is logic `1` or `0`. Can also use `True` or `False` as inputs to the value function. 

```python
#logic high
output_pin.value(1)

#logic low
output_pin.value(0)
```

## Input Pin Setup

To set any of the GPIO pins as an `input` pin, use the following lines (assuming setting up GPIO 4 as an input pin):

```python
from machine import Pin

input_pin = Pin(4, Pin.IN)
```
These lines setup the variable named `input_pin` as an instance of the Pin class, the inputs to the setup function are the number of the pin, `4`, and the direction of the pin `Pin.IN`. 

To read the value of the pin we setup, use the `value()` function. 

```python
while True:
    print(input_pin.value())
```

Important to note: when there is no electronic connection plugged into the Pin, the print reading will print both 0 and 1 because there is no set default state. 

## Adding Default State to an Input Pin
Input pins do not have a default state, if there is no default state set, a pin is called `floating`. 

To add a `default state` to an input pin, we can use a `pull-up` or `pull-down` resistor. 

### Pull-Up

If the `default state` of an input signal is `logic-high`, we use a `pull-up` resistor on the gpio pin. 

Example of setting up Pin `5` as an input pin with a pull-up resistor:

```python
from machine import Pin

input_pin = Pin(5, Pin.IN, Pin.PULL_UP)

while True:
    print(input_pin.value()) #default = 1
```
### Pull-Down

If the `default state` of an input signal is `logic-low`, we use a `pull-down` resistor on the gpio pin. 

Example of setting up Pin `2` as an input pin with a pull-down resistor:

```python
from machine import Pin

input_pin = Pin(2, Pin.IN, Pin.PULL_DOWN)

while True:
    print(input_pin.value()) #default = 0
```



