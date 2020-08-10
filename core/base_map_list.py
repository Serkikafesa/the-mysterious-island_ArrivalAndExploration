# coding: utf-8


# Code 

# Load the a new map from the base_map.txt
def initial_map():
    """
        Load the map from the base_map.txt
    """

    base_map_list = []

    # Open the map file
    try:
        with open("mods/maps/base_map.txt", "r", encoding="utf-8") as map:
            for line in map:
                #print(line)
                for char in line:
                    if char != "\n":
                        base_map_list.append(char)
                        
            #print(base_map_list)
    except:
        print("Impossible de charger la carte")

initial_map()
