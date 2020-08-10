# coding: utf-8

# Imports

import core.game as game
import core.variables as variables
import mods


# Game flow

def game_launch():
    """
        Principal gameflow
    """
    # Initialize game
    game.show_title_and_rules()
    # Display main menu
    # Load and print the map
    game.initial_map()
    game.draw_map()

    # main game loop
    while variables.game_in_progress:
        game.get_character_action()

    # game end
    print("\nAu revoir.\n")




if __name__ == "__main__":
    game_launch()
