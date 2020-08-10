# coding: utf-8

# Imports

import core.sphynx as sphynx
import core.caesar as caesar
import core.fizz_buzz as fizz_buzz
import mods.visuals.visuals_fr_fr as visuals
import core.variables as variables
import core.utilities as utilities


def show_title_and_rules():
    """
        Prints title ans rules
    """

    utilities.clear_console()

    visuals.game_logo()
    print("\n")

    print ("Pour te déplacer, tu as ces touches :")
    print ("Z (Haut), S (Bas), Q (Gauche), D (Droite) ou C (Quitter)\n")


# Load the a new map from the base_map.txt
def initial_map():
    """
        Load the map from the base_map.txt
    """


    # Open the map file
    try:
        with open("mods/maps/base_map.txt", "r", encoding="utf-8") as map:
            Y = 0
            for line in map:
                columns = []
                X = 0
                for char in line:
                    # add character to map
                    if char != "\n":
                        columns.append(char)
                    # place character at map entry
                    if character == "E":
                        variables.character_position["X"] = X
                        variables.character_position["Y"] = Y
                    X += 1
                    
                # add line to map
                variables.game_map.append(columns)
                Y += 1
                        

    except FileNotFoundError:
        variables.game_in_progress = False
        print("Impossible de charger la carte")



def draw_map():
    """
        Draw map on console from 2 dimensional list
    """

    # draw maze
    for Y in range(len(variables.game_map)):
        for X in range(len(variables.game_map[Y])):
            if (Y == variables.character_position["Y"]
                and X == variables.character_position["X"]):
                # this is character position, draw it
                print(variables.character_symbol, end="")
            else:
                # no character here, draw maze
                print(variables.map_elements[variables.game_map[Y][X]]["Icon"], end="")
        print()

    # show message if any
    if variables.game_message != "":
        print(variables.game_message)
        variables.game_message = ""
    else:
        print()

    # show game data
    print(f"Nombre d'actions effectuées : {variables.character_total_actions} (dont {variables.character_bad_actions} mauvaises)\n")


def get_character_action():
    """
        Ask for character action
    """

    # list of possible actions
    possible_actions = ["Z", "S", "Q", "D", "C"]

    # wait for a valid action
    action = ""
    while action not in possible_actions:
        action = input("Que doit faire le personnage ? ").upper()

    # execute action
    execute_character_action(action)

    # refresh maze
    game.show_title_and_rules()
    game.draw_map()


def execute_character_action(action):
    """
        Executes choosen action
    """

    # store new character position
    new_character_possitionX = variables.character_position["X"]
    new_character_possitionY = variables.character_position["Y"]

    # prepare action
    if action == "Z":
        variables.character_total_actions += 1
        new_character_possitionY -= 1
        variables.game_message = "\nLe personnage se déplace vers le haut\n"
    elif action == "S":
        variables.character_total_actions += 1
        new_character_possitionY += 1
        variables.game_message = "\nLe personnage se déplace vers le bas\n"
    elif action == "Q":
        variables.character_total_actions += 1
        new_character_possitionX -= 1
        variables.game_message = "\nLe personnage se déplace vers la gauche\n"
    elif action == "D":
        variables.character_total_actions += 1
        new_character_possitionX += 1
        variables.game_message = "\nLe personnage se déplace vers la droite\n"
    elif action == "C":
        variables.game_message = "\nTu as choisi d'abandonner le jeu !\n"
        variables.game_in_progress = False
        return

    # check if action is allowed
    if (new_character_possitionY < 0
        or new_character_possitionY >= len(variables.game_map)
        or new_character_possitionX < 0 
        or new_character_possitionX >= len(variables.game_map[0])):
        # new position is out of map, can't move
        variables.game_message = "\nImpossible d'aller par là !\n"
        variables.character_bad_actions += 1
        return
    elif not variables.map_elements[
        variables.game_map[new_character_possitionY][new_character_possitionX]]["CanWalk"]:
        # new position blocks movement, can't move
        variables.game_message = f"\nAïe, un {variables.map_elements[variables.game_map[new_character_possitionY][new_character_possitionX]]['Name']} !\n"
        variables.character_bad_actions += 1
        return
    elif variables.game_map[new_character_possitionY][new_character_possitionX] == "X":
        # player quits
        variables.game_message = "\nBRAVO, tu es sorti du labyrinthe !"
        variables.game_in_progress = False
        return

    # execute action
    variables.character_position["X"] = new_character_possitionX
    variables.character_position["Y"] = new_character_possitionY
