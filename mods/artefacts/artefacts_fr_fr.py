# coding: utf-8

# Initial artefacts contains in the backpack/inventory

initial_artefatcts_dict = {

    'swiss_knife' : {
        'usable' : False,
        'message' : "L'objet est tranchant et ce n'est pas le moment...",
        'error' : ""
    },
    'laptop' : {
        'usable' : True,
        'message' : "Regarder des photos de famille, quel plaisir !",
        'error' : ""
    },
    'bottle' : {
        'usable' : True,
        'message' : "L'objet est tranchant et ce n'est pas le moment...",
        'error' : "Je ne crois que ce soit possible de remplir avec ça..."
    },
    'solar_panel' : {
        'usable' : True,
        'message' : "Est-ce vraiment le moment pour recharger ton ordinateur !?!",
        'error' : ""
    },
    'partchement_map' : {
        'usable' : True,
        'message' : "Une carte arrivée par hasard dans ton sac, curieux...",
        'error' : ""
    }

}

print(initial_artefatcts_dict['swiss_knife']['crazy'])

collectibles_dict = {
    'coconut' : {
        'usable' : False,
        'message' : "Ouvrir une noix de coco est épuisant...",
        'error' : ""
        'edible' : True,
        'hydratation' : 15,
        'saciety' : 15,
        'energy' : 15
    },
    'banana' : {
        'usable' : False,
        'message' : "Banana split... ou presque !",
        'error' : ""
        'edible' : True,
        'hydratation' : 2,
        'saciety' : 25,
        'energy' : 20
    },
    'edible_root' : {
        'usable' : False,
        'message' : "Miam, la meilleure racine que tu aies jamais mangé !",
        'error' : ""
        'edible' : True,
        'hydratation' : 5,
        'saciety' : 5,
        'energy' : 10
    },
    'hiking_pack' : {
        'usable' : True,
        'message' : "Tu as désormais deux fois plus de place dans ton sac mais cela te fatigue plus !",
        'error' : ""
        'edible' : False,
        'hydratation' : 0,
        'saciety' : 0,
        'energy' : -3
    }
        'bronze_key' : {
        'usable' : True,
        'message' : "Tu as récupérer la clef du sphynx",
        'error' : ""
        'edible' : False,
        'hydratation' : 0,
        'saciety' : 0,
        'energy' : 0
    }

}