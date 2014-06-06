from Click_Press import *
from Cooldown import Cooldown
from Status import is_status_active, get_status, get_pixel_sum, get_pixel_sum_color
import logging
from Settings import Settings
logger = logging.getLogger(__name__)
Gem_Collection = {}
Item_Collection = {}


def activate_gem():
    mousePos(Cord.Item_cat_loc)
    leftClick()
    mousePos(Cord.gem_loc)
    leftClick()
    mousePos(Cord.Item_cat_loc)
    leftClick()


def get_gem():
    mousePos(Cord.Item_cat_loc)
    leftClick()
    time.sleep(0.3)
    item = Cord.ibox_gem
    sum = get_pixel_sum(item)
    result = Gem_Collection.get(sum)
    if result is not None:
        if result == "Health_Gem":
            logging.debug("health gem found")
            Cooldown.h_gem = True
        elif result == "Mana_Gem":
            logging.debug("mana gem found")
            Cooldown.m_gem = True
        elif result == "Spirit_Gem":
            logging.debug("spirit gem found")
            Cooldown.s_gem = True
        elif result == "Mystic_Gem" and not is_status_active("Channeling"):
            logging.debug("mystic gem found")
            mousePos(Cord.gem_loc)
            leftClick()
    else:
        logger.warning("UNKNOWN gem: %d" % sum)
        get_pixel_sum_color(item, True)
        #REMOVE ONCE ALL GEMS ARE FOUND
        mousePos(Cord.gem_loc)
        leftClick()
        if Settings.shutdown:
            logging.critical("unknown gem, shutting down")
            quit()
    mousePos(Cord.Item_cat_loc)
    leftClick()


def get_gem_original():
    mousePos(Cord.Item_cat_loc)
    leftClick()
    time.sleep(0.3)
    item = Cord.ibox_gem
    sum = get_pixel_sum(item)
    if sum == 713603:
        logging.debug("health gem found")
        Cooldown.h_gem = True
        get_pixel_sum_color(item, True)
    elif sum == 729967 or sum == 729940:
        logging.debug("mana gem found")
        Cooldown.m_gem = True
        get_pixel_sum_color(item, True)
    elif sum == 723194 or sum == 722448 or sum == 723149:
        logging.debug("spirit gem found")
        Cooldown.h_gem = True
        get_pixel_sum_color(item, True)
    elif (sum == 722692 or sum == 722641) and not is_status_active("Channeling"):
        logging.debug("mystic gem found")
        get_pixel_sum_color(item, True)
        mousePos(Cord.gem_loc)
        leftClick()
    elif sum == 865970 or sum == 1480:  # empty
        ""
        #logging.debug("no gem found")
    else:
        logger.warning("UNKNOWN gem: %d" % sum)
        get_pixel_sum_color(item, True)
        mousePos(Cord.gem_loc)
        leftClick()
        if Settings.shutdown:
            logging.critical("unknown gem, shutting down")
            quit()
    mousePos(Cord.Item_cat_loc)
    leftClick()


# 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
def get_items_original():
    Cord.Items = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    mousePos(Cord.Item_cat_loc)
    leftClick()
    time.sleep(1.0)
    count = 1
    for item in Cord.ibox_list:
        sum = get_pixel_sum_color(item, False)
        if is_pot(Cord.h_potions, sum):
            Cord.Items[count - 1] = 0
        elif is_pot(Cord.m_potions, sum):
            Cord.Items[count - 1] = 1
        elif is_pot(Cord.s_potions, sum):
            Cord.Items[count - 1] = 2
        elif sum == 865970:  # empty
            Cord.Items[count - 1] = 9
        else:
            logger.warning("UNKNOWN item %d: %d" % (count, sum))
            get_pixel_sum_color(item, True)
            Cord.Items[count - 1] = 9
            #if Settings.shutdown:
            #    logging.critical("unknown element, shutting down")
            #    quit()
        count += 1
    mousePos(Cord.Item_cat_loc)
    leftClick()
    #print Cord.Items


# 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
def get_items():
    Cord.Items = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    mousePos(Cord.Item_cat_loc)
    leftClick()
    time.sleep(1.0)
    count = 1
    for item in Cord.ibox_list:
        sum = get_pixel_sum_color(item, False)
        result = Item_Collection.get(sum)
        if result == "Health_Pot":
            Cord.Items[count - 1] = 0
        elif result == "Mana_Pot":
            Cord.Items[count - 1] = 1
        elif result == "Spirit_Pot":
            Cord.Items[count - 1] = 2
        elif result == "Empty" or result == "Used":  # empty
            Cord.Items[count - 1] = 9
        else:
            logger.warning("UNKNOWN item %d: %d" % (count, sum))
            get_pixel_sum_color(item, True)
            Cord.Items[count - 1] = 9
            #if Settings.shutdown:
            #    logging.critical("unknown element, shutting down")
            #    quit()
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
        item_name = "Health_Pot"
    elif item == 1:
        item_name = "Mana_Pot"
    elif item == 2:
        item_name = "Spirit_Pot"
    if is_status_active(item_name):
        return True
    else:
        time.sleep(2)
        get_status()
        return is_status_active(item_name)


def leftover_inventory():
    count = 0
    h_count = 0
    m_count = 0
    s_count = 0
    for item in Cord.Items:
        if item != 9:
            count += 1
            if item == 0:
                h_count += 1
            elif item == 1:
                m_count += 1
            elif item == 2:
                s_count += 1
    logger.info("Inventory Leftover: " + str(count))
    logger.info("Health Potions: " + str(h_count))
    logger.info("Mana Potions: " + str(m_count))
    logger.info("Spirit Potions: " + str(s_count))

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
            logger.info("No Spirit Potions Left")
            Cooldown.s_potion = 999
            return False
    else:
        return False


#0 = health, 1 = mana, 2 = spirit
def use_gem(gem_type, current):
    if gem_type == 0:
        if current <= 60 and Cooldown.h_gem:
            activate_gem()
            Cooldown.h_gem = False
            return True
    elif gem_type == 1:
        if current <= 40 and Cooldown.m_gem:
            activate_gem()
            Cooldown.m_gem = False
            return True
    elif gem_type == 2:
        if current <= 80 and Cooldown.s_gem:
            activate_gem()
            Cooldown.s_gem = False
            return True
    return False


def use_item(item_type):
    for i in range(0, len(Cord.Items)):
        if Cord.Items[i] == item_type:
            Cord.Items[i] = 9
            mousePos(Cord.Item_cat_loc)
            leftClick()
            mousePos(Cord.item_locs[i])
            leftClick()
            return
    logging.warning("Item Not Found...")