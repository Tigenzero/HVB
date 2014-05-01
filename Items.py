from Click_Press import *
from Cooldown import Cooldown
from Status import is_status_active, get_status, get_pixel_sum_color
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
def get_items():
    Cord.Items = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    mousePos(Cord.Item_cat_loc)
    leftClick()
    time.sleep(0.3)
    count = 1
    for item in Cord.ibox_list:
        sum = get_pixel_sum_color(item, False)
        if is_pot(Cord.h_potions, sum):
            Cord.Items[count - 1] = 0
        elif is_pot(Cord.m_potions, sum):
            Cord.Items[count - 1] = 1
        elif is_pot(Cord.s_potions, sum):
            Cord.Items[count - 1] = 2
        else:
            print "UNKNOWN item %d: %d" % (count, sum)
            get_pixel_sum_color(item, True)
            Cord.Items[count - 1] = 9

        count += 1
    mousePos(Cord.Item_cat_loc)
    leftClick()
    #print Cord.Items


def is_pot(pots, value):
    for pot in pots:
        if pot == value:
            return True
    return False


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
    if is_status_active(item_name):
        return True
    else:
        time.sleep(2)
        get_status()
        return is_status_active(item_name)


def use_health_pot(current_health):
    if current_health <= 40:
        if not is_item_active(0):
            if have_item(0):
                use_item(0)
                return True
    return False


def use_mana_pot(current_mana):
    if current_mana <= 20:
        if not is_item_active(1):
            if have_item(1):
                use_item(1)
                return True
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