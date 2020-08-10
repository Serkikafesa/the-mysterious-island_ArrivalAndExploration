# coding: utf-8


# Imports

import mods.visuals.visuals_fr_fr as visuals
import mods.languages.languages_fr_fr as languages
import core.utilities as utilities


# Code

def launch_caesar():

    utilities.clear_console()

    # Caesar display logo et rules
    visuals.caesar_logo()
    languages.caesar_rules()

    caesar_victory = False

    # Part of Python zen
    zen_python = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."

    print(zen_python)

    # Length of an object, here zen_python
    zen_length = len(zen_python)

    char_list = []

    encryption_key = 3

    # Loop to encrypt message
    for char in range(zen_length):

        # If the character is alphabetical
        if zen_python[char].isalpha():
            # Value in the ASCII table of each character
            tmp = ord(zen_python[char])
            # Add encryption key to the value of ASCII table
            tmp_encrypted = tmp + encryption_key
            # Verify if value of character exit the alphabetical part of ASCII table and loop at beginning (example: z + 3 = c)
            if (tmp_encrypted) > 122:
                tmp_encrypted -= 26  
            # Add characters to list
            char_list.append(chr(tmp_encrypted))

        # When character isn't alpha, put it like that in the list
        else:
            char_list.append(zen_python[char])
        #print(d)

    # Recreate sentence in an encrypted version
    result = ''.join(char_list)

    print(result)