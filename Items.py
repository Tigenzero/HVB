from Click_Press import *
from Cooldown import Cooldown
from Status import is_status_active, get_status


def have_item(item_type):
    for i in range(0, len(Cord.Items)):
    #for item in Cord.Items:
        if Cord.Items[i] == item_type:
            return True
    return False


def is_item_active(item):
    get_status()
    item_name = ''
    if item == 0:
        item_name = "health_pot"
    elif item == 1:
        item_name = "mana_pot"
    elif item == 2:
        item_name = "spirit_pot"
    return is_status_active(item_name)


def use_health_pot(current_health):
    if not is_item_active(0):
        if current_health <= 40:
            if have_item(0):
                print "Using Health Potion"
                use_item(0)
                return True
            else:
                print "No Health Potions Left"
                Cooldown.h_potion = 999
    return False


def use_mana_pot(current_mana):
    if not is_item_active(1):
        if current_mana <= 20:
            if have_item(1):
                print "Using Mana Potion"
                use_item(1)
                return True
            else:
                print "No Mana Potions Left"
                Cooldown.m_potion = 999
    return False


def use_spirit_pot(current_spirit):
    if current_spirit <= 10 and Cooldown.s_potion <= 0:
        if have_item(2):
            print "Using Spirit Potion"
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
    mousePos(Cord.Item_cat_loc)
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