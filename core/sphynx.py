# coding: utf-8


# Imports

import random
import mods.visuals.visuals_fr_fr as visuals
import mods.languages.languages_fr_fr as languages


# Code

def launch_sphynx():

    sphynx_victory = False

    visuals.sphynx_logo()
    languages.sphynx_rules()
    languages.sphynx_question()

    print("Tu peux répondre par 'Oui' ou 'Non':")
    user_answer = str(input())


    # not user_answer.isalpha() and user_answer != "Oui" or not user_answer.isalpha() and user_answer != "Non" :

    a = 1

    while (a) :
        if user_answer == "Oui":
            a = 0
            # The sphynx calculate a random number
            sphynx_number = random.randint(0, 100)

            # Ask user a number
            for repeat_ask in range(20):
                print("Veux-tu bien rentrer un nombre entre 1 et 100 ?")
                user_number = int(input())

                # Compare the sphynx_number and user_number
                if sphynx_number > user_number:
                    print("Le nombre que j'ai en tête est plus grand")
                elif sphynx_number < user_number:
                    print("Le nombre que j'ai en tête est plus petit")
                else:
                    print("Tu as trouvé le bon nombre, serais-tu devin ?")
                    return right_number

            right_number = find_number(counter)

            while right_number < 3 :
                find_number(right_number)

        elif user_answer == "Non":
            a = 0
            break
        else:
            print("Tu dois répondre par 'Oui' ou 'Non'")
            user_answer = str(input())

