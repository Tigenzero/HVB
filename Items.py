from Click_Press import *
from Cooldown import Cooldown


def have_item(item_type):
    for i in range(0, len(Cord.Items)):
    #for item in Cord.Items:
        if Cord.Items[i] == item_type:
            return True
    return False


def use_health_pot(current_health):
    if current_health <= 40 and Cooldown.h_potion <= 0:
        if have_item(0):
            print "Using Health Potion"
            use_item(0)
            Cooldown.h_potion = 20
            return True
        else:
            print "No Health Potions Left"
            Cooldown.h_potion = 999
            return False
    else:
        return False


def use_mana_pot(current_mana):
    if current_mana <= 10 and Cooldown.m_potion <= 0:
        if have_item(1):
            use_item(1)
            Cooldown.m_potion = 20
            return True
        else:
            print "No Mana Potions Left"
            Cooldown.m_potion = 999
            return False
    else:
        return False


def use_spirit_pot(current_spirit):
    if current_spirit <= 10 and Cooldown.s_potion <= 0:
        if have_item(2):
            use_item(2)
            Cooldown.s_potion = 20
            return True
        else:
            print "No Spirit Potions Left"
            Cooldown.s_potion = 999
            return False
    else:
        return False


def use_gem():
    mousePos(Cord.Item_cat_loc)
    leftClick()
    mousePos(Cord.gem_loc)
    leftClick()


def use_item(item_type):
    for i in range(0, len(Cord.Items)):
        if Cord.Items[i] == item_type:
            Cord.Items[i] = 9
            mousePos(Cord.Item_cat_loc)
            leftClick()
            mousePos(Cord.item_locs[i])
            leftClick()
            return
    print "Item Not Found..."