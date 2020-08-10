# coding: utf-8


# Imports

import random
import mods.visuals.visuals_fr_fr as visuals
import mods.languages.languages_fr_fr as languages
import core.utilities as utilities

# Code

def launch_fizz_buzz():

    utilities.clear_console()

    # Fizz-Buzz display logo et rules
    visuals.fizz_buzz_logo()
    languages.fizz_buzz_rules()

    fizz_buzz_victory = False

    b = 15 

    z1 = b % 5

    if z1 == 0:
        print("Fizz")

    #print(z1)

    z2 = b % 3 

    if z2 == 0:
        print("Buzz")

    #print(z2)

    if z1 == 0 and z2 == 0:
        print("Fizz Buzz")