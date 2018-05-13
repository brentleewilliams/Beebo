#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import textwrap

compliments = [
"You are an awesome friend.",
"You are a gift to those around you.",
"You are a smart cookie.",
"You are awesome!",
"You have impeccable manners.",
"I like your style.",
"You have the best laugh.",
"I appreciate you.",
"You are the most perfect you there is.",
"You are enough.",
"You are strong.",
"Your perspective is refreshing.",
"I am grateful to know you.",
"You light up the room.",
"You deserve a hug right now.",
"You should be proud of yourself.",
"You are more helpful than you realize.",
"You have an awesome sense of humor!",
"You are really courageous.",
"Your kindness is a balm to all who encounter it.",
"You are all that and a super-size bag of chips.",
"Where did you get that shirt... I love it!",
"Son, I am proud of you.",
"I want to be you when I grow up.",
"You have inspired me and changed my life.",
"If I was stuck on a deserted island and could only bring three things you are one of them.",
"ARE YOU SURE YOU HAVE NEVER DONE THIS BEFORE?",
"I need you for everything.",
"Your smile is contagious",
"You raise the bar",
"You walk the walk and talk the talk",
"You throw a great party",
"You never cease to amaze me",
"If you were a dinosaur, you would be a trex(arguably the best one).",
"Thats a great idea!",
"Beebo loves you",
"You are as a great as a cup of coffee",
"GET MONEY WHITE BOY",
"Home is whereever I am with you",
"Even when I don't want to talk, I like talking to you",
"When you are not around, I tell all my robot friends how great you are.",
"Your face. I like it.",
"If I had legs, I would give you a standing ovation.",
"Watch out. I am gonna kiss you.",
"10 out of 10.",
"Error 404: You are too great to compliment. There are no words.",
"Beep boop bop beep boop. (That’s robot for “You are super awesome!”)",
"You are a gentleman and a scholar.",
"You have the most boop-worthy nose.",
"I am sure everyone around you is intimidated by your high intellect."
]

# Randomize and put into a string
compliment = random.choice(compliments)

# Wrap selected string.
wrapper = textwrap.TextWrapper(width=50)
word_list = wrapper.wrap(text=compliment)


# Print each line of wrapped string
for element in word_list:
    print(element)
