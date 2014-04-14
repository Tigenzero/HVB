#Styles: Dual-wield:0, 1-handed:1, 2-handed:2, mage:3, niken:4
class Player_0:
    style = 0
    # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    Items = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1] #main character
    Cure = 0
    special_attack = [8, 9, 10]
    Iris_Strike = 8 #deprecated
    Backstab = 9 #deprecated
    Frenzied_Blows = 10 #deprecated
    Regen = 4
    Protection = -1
    #unused
    shield_bash = -1
    shockblast = -1
    premium = [12, 13]


class Player_1:
    style = 1
    Cure = 0
    shield_bash = 1
    #unused
    Iris_Strike = -1 #deprecated
    Regen = -1
    Protection = -1 #3 (costs to much mana)
    shockblast = -1
    special_attack = [1, -1, -1]
     # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    # Health has 30 round cooldown, Mana and Spirit have 15 round cooldown
    Items = [0,0,0,0,0,0,9,9,9] #Current Items in your Battle Inventory
    premium = [3, -1]