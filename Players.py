#Styles: Dual-wield:0, 1-handed:1, 2-handed:2, mage:3, niken:4
class Player_0:
    name = "Player_0"
    style = 0
    # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    #Items = (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1) #main character
    special_attack = [5, 6, 7]
    premium = ["Heartseeker", "Spirit_Shield", "Absorb"]
    skills = ["Cure", "Regen", "Heartseeker", "Spirit_Shield", "Absorb", "Special", "Special", "Special", "Blind", "Drain", "Weaken", "Sleep", "Empty", "Empty", "Empty", "Empty"]

class Player_1:
    name = "Player_1"
    style = 1
    special_attack = [1, 2, 8]
     # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    # Health has 30 round cooldown, Mana and Spirit have 15 round cooldown
    #Items = (0, 0, 0, 1, 1, 1, 1, 9, 9) #Current Items in your Battle Inventory
    premium = ["Protection", "Shadow_Veil", "Haste", "Spark_Life"]
    skills = ["Cure", "Special", "Special", "Protection", "Haste", "Regen", "Shadow_Veil", "Spark_Life", "Special", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"]

class Player:
    name = ""
    style = ""
    spirit = False
    # 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
    items = () #main character
    special_attack = []
    premium = []
    skills = []
