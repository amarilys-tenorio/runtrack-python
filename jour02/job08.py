def afficher_fruit(type, saison):
    if type == "fruits":
        if saison == "hiver":
            print ("orange, mandarine, et kiwi")
        elif saison == "été":
            print ("poire, fraise et cassis")
    elif type == "legume":
        if saison == "hiver":
            print ("carotte, topinambour, endive")
        elif saison == "été":
            print ("artichaut, aubergine et navet")

afficher_fruit("fruits", "hiver")