#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import textwrap

compliments = [
"You won a t-shirt!",
"Tote bag, awesome!",
"Sorry you didn't win this time :(."
]

# Randomize and put into a string
compliment = random.choice(compliments)

# Wrap selected string.
wrapper = textwrap.TextWrapper(width=50)
word_list = wrapper.wrap(text=compliment)


# Print each line of wrapped string
for element in word_list:
    print(element)
