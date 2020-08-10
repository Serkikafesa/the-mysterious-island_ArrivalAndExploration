# coding: utf-8

# Character

character_symbol = "☼"
character_position = {"X" : 59, "Y" : 24}
character_total_actions = 0
character_bad_actions = 0


# map (map_elements is a dictionary of dictionaries)
game_map = []
map_elements = {
    " " : {
        "Name" : "sol",
        "Icon" : " ",
        "CanWalk" : True},
    "♣" : {
        "Name" : "arbre",
        "Icon" : "♣",
        "CanWalk" : False},
    "▲" : {
        "Name" : "montagne",
        "Icon" : "▲",
        "CanWalk" : False
        },
    "~" : {
        "Name" : "riviere",
        "Icon" : "~",
        "CanWalk" : False
        },
    "█" : {
        "Name" : "ocean",
        "Icon" : "█",
        "CanWalk" : False
        },
    "╔" : {
        "Name" : "pont",
        "Icon" : "╔",
        "CanWalk" : True
        },
    "═" : {
        "Name" : "pont",
        "Icon" : "═",
        "CanWalk" : True
    },
    "╗" : {
        "Name" : "pont",
        "Icon" : "╗",
        "CanWalk" : True
    },
    "░" : {
        "Name" : "plage",
        "Icon" : "░",
        "CanWalk" : True
        },
    "?" : {
        "Name" : "quete",
        "Icon" : "?",
        "CanWalk" : True
        },
    "E" : {
        "Name" : "entrée",
        "Icon" : "E",
        "CanWalk" : True
        },
    "X" : {
        "Name" : "sortie",
        "Icon" : "X",
        "CanWalk" : True
        }
    }


# Sphynx Challenge

sphynx_position = {"X" : 64, "Y" : 4}


# Caesar Challenge

caesar_position = {"X" : 42, "Y" : 27}


# Fizz-buzz Challenge

fizz_buzz_position = {"X" : 9, "Y" : 24}


# Game
game_in_progress = True
game_message = ""