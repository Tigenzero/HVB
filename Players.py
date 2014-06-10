#Styles: Dual-wield:0, 1-handed:1, 2-handed:2, mage:3, niken:4
class Player_0:
    style = 0
    # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    #Items = (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1) #main character
    special_attack = [5, 6, 7]
    premium = ["Heartseeker", "Spirit_Shield", "Absorb"]


class Player_1:
    style = 1
    special_attack = [1, 2, -1]
     # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    # Health has 30 round cooldown, Mana and Spirit have 15 round cooldown
    #Items = (0, 0, 0, 1, 1, 1, 1, 9, 9) #Current Items in your Battle Inventory
    premium = ["Protection", "Haste", "Regen", "Shadow_Veil"]