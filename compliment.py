#!/usr/bin/python
# -*- coding: utf-8 -*-

from Adafruit_Thermal import *
import random

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
"You're strong.",
"Your perspective is refreshing.",
"I'm grateful to know you.",
"You light up the room.",
"You deserve a hug right now.",
"You should be proud of yourself.",
"You're more helpful than you realize.",
"You have a great sense of humor.",
"You've got an awesome sense of humor!",
"You are really courageous.",
"Your kindness is a balm to all who encounter it.",
"You're all that and a super-size bag of chips.",
"Where'd you get that shirt... I love it!",
"Son, I’m proud of you.",
"I want to be you when I grow up.",
"You have inspired me and changed my life.",
"If I was stuck on a deserted island and could only bring three things you're one of them.",
"ARE YOU SURE YOU'VE NEVER DONE THIS BEFORE?",
"I need you for everything.",
"Your smile is contagious",
"You raise the bar",
"You walk the walk and talk the talk",
"You thre a great party",
"You never cease to amaze me",
"If you were a dinosaur, you would be a trex(arguably the best one).",
"Thats a great idea!",
"Beebo loves you",
"You're as a great as a cup of coffee",
"GET MONEY WHITE BOY",
"Home is whereever I'm with you",
"Even when I don't want to talk, I like talking to you"
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
