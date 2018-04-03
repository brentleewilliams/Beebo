#!/usr/bin/python

from Adafruit_Thermal import *
import random
#!/usr/bin/env python
# -*- coding: utf-8 -*-
....


compliments = [
"You're an awesome friend.",
"You're a gift to those around you.",
"You're a smart cookie.",
"You are awesome!",
"You have impeccable manners.",
"I like your style.",
"You have the best laugh.",
"I appreciate you.",
"You are the most perfect you there is.",
"You are enough.",
"You're strong."
]

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

# Test inverse on & off
printer.feed(2)
printer.inverseOn()
printer.println(random.choice(compliments))
printer.inverseOff()
printer.feed(3)

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults



