# coding: utf-8

# Character

character_symbol = "☼"
character_position = {"X" : 0, "Y" : 0}
character_total_actions = 0
character_bad_actions = 0


# map (map_elements is a dictionary of dictionaries)
game_map = []
map_elements = {
    " " : {
        "Name" : "sol",
        "Icon" : " ",
        "CanWalk" : True},
    "T" : {
        "Name" : "arbre",
        "Icon" : "♣",
        "CanWalk" : False},
    "M" : {
        "Name" : "montagne",
        "Icon" : "▲",
        "CanWalk" : False
        },
    "R" : {
        "Name" : "riviere",
        "Icon" : "~",
        "CanWalk" : False
        },
    "O" : {
        "Name" : "ocean",
        "Icon" : "█",
        "CanWalk" : False
        },
    "B" : {
        "Name" : "pont",
        "Icon1" : "╔══╗",
        "CanWalk" : True
        },
    "S" : {
        "Name" : "plage",
        "Icon" : "░",
        "CanWalk" : True
        },
    "Q" : {
        "Name" : "quete",
        "Icon" : "?",
        "CanWalk" : False
        },
    "E" : {
        "Name" : "entrée",
        "Icon" : " ",
        "CanWalk" : True
        },
    "X" : {
        "Name" : "sortie",
        "Icon" : "X",
        "CanWalk" : True
        }
    }


# Game
game_in_progress = True
game_message = ""