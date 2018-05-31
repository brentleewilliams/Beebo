#!/usr/bin/python
# -*- coding: utf-8 -*-

from Adafruit_Thermal import *
import random
import textwrap

compliments = [
"You won a t-shirt!",
"Tote bag, awesome!",
"Sorry you didn't win this time :(."
]

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

# Test inverse on & off
printer.feed(2)
printer.inverseOn()
printer.println(random.choice(compliments))
printer.inverseOff()
printer.feed(4)

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults