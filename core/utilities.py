# coding: utf-8


# Imports

import os
import sys

# Function to get data


# Function to format data


# Clear terminal window

def clear_console():
    """
        This function clears the console depending on OS
    """

    if "win" in sys.platform.lower():
        # for windows
        os.system("cls")
    elif "linux" in sys.platform.lower():
        # for linux
        os.system("clear")
