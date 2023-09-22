"""
Created by: Angelo Yaluyng
Created on: Sep 2023
This module takes the temperature of the MicroBit
"""
from microbit import *
import random

# our variable for a random number
temperature = 0

display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        temperature = temperature()
        display.show(str(temperature))
