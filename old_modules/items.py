import logging

from user_interface.click_press import *
from Status import is_status_active, get_status, get_pixel_sum, get_pixel_sum_color
import Settings

logger = logging.getLogger(__name__)
Gem_Collection = {}
Item_Collection = {}


class Items:
    h_gem = False
    s_gem = False
    m_gem = False
    cool_down = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def activate_gem():
    open_items()
    mouse_position(Cord.gem_loc)
    left_click()
    #mouse_position(Cord.Item_cat_loc)
    #left_click()


def cool_down():
    for item in Items.cool_down:
        if item > 0:
            item -= 1


def dynamic_get_gem():
    open_items()
    item = Cord.ibox_gem
    sum = get_pixel_sum_color(item)
    result = Gem_Collection.get(sum)
    if result is not None:
        if result == "Health_Gem":
            logging.debug("health gem found")
            get_pixel_sum_color(item, True)
            Items.h_gem = True
        elif result == "Mana_Gem":
            logging.debug("mana gem found")
            get_pixel_sum_color(item, True)
            Items.m_gem = True
        elif result == "Spirit_Gem":
            logging.debug("spirit gem found")
            get_pixel_sum_color(item, True)
            Items.s_gem = True
        elif result == "Mystic_Gem" and not is_status_active("Channeling"):
            logging.debug("mystic gem found")
            get_pixel_sum_color(item, True)
            mouse_position(Cord.gem_loc)
            left_click()
    else:
        logger.warning("UNKNOWN gem: %d" % sum)
        get_pixel_sum_color(item, True)
        #REMOVE ONCE ALL GEMS ARE FOUND
        mouse_position(Cord.gem_loc)
        left_click()
        if Settings.shutdown:
            logging.critical("unknown gem, shutting down")
            quit()
    mouse_position(Cord.Item_cat_loc)
    left_click()


def get_gem():
    open_items()
    item = Cord.ibox_gem
    sum = get_pixel_sum_color(item)
    message = "no gem found"
    if 710000 <= sum <= 719999:
        #logging.debug("health gem found")
        message = "health gem found"
        Items.h_gem = True
    elif 729000 <= sum <= 729999:
        #logging.debug("mana gem found")
        message = "mana gem found"
        Items.m_gem = True
    elif 723000 <= sum <= 723999:
        #logging.debug("spirit gem found")
        message = "spirit gem found"
        Items.s_gem = True
    elif 722000 <= sum <= 722999 and not is_status_active("Channeling"):
        message = "Channeling gem found"
        mouse_position(Cord.gem_loc)
        left_click()
    mouse_position(Cord.Item_cat_loc)
    left_click()
    return message


def get_gem_original():
    mouse_position(Cord.Item_cat_loc)
    left_click()
    time.sleep(0.3)
    item = Cord.ibox_gem
    sum = get_pixel_sum(item)
    if sum == 713603:
        logging.debug("health gem found")
        Items.h_gem = True
        get_pixel_sum_color(item, True)
    elif sum == 729967 or sum == 729940:
        logging.debug("mana gem found")
        Items.m_gem = True
        get_pixel_sum_color(item, True)
    elif sum == 723194 or sum == 722448 or sum == 723149:
        logging.debug("spirit gem found")
        Items.h_gem = True
        get_pixel_sum_color(item, True)
    elif (sum == 722692 or sum == 722641) and not is_status_active("Channeling"):
        logging.debug("mystic gem found")
        get_pixel_sum_color(item, True)
        mouse_position(Cord.gem_loc)
        left_click()
    elif sum == 865970 or sum == 1480:  # empty
        ""
        #logging.debug("no gem found")
    else:
        logger.warning("UNKNOWN gem: %d" % sum)
        get_pixel_sum_color(item, True)
        mouse_position(Cord.gem_loc)
        left_click()
        if Settings.shutdown:
            logging.critical("unknown gem, shutting down")
            quit()
    mouse_position(Cord.Item_cat_loc)
    left_click()


# 0 = Health, 1 = Mana, 2 = Spirit, 9 = used
def dynamic_get_items():
    Cord.Items = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    mouse_position(Cord.Item_cat_loc, True)
    left_click()
    time.sleep(0.7)
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
    mouse_position(Cord.Item_cat_loc, True)
    left_click()
    #print Cord.Items


def get_items():
    #Cord.Items = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    Cord.Items = list(Settings.Player.items)
    logging.debug(Cord.Items)
    #Settings Items as static until further notice.
    """open_item_tab()
    count = 1
    for item in Cord.ibox_list:
        if is_slot_empty_or_used(item):
            Cord.Items[count - 1] = 9
        count += 1
    close_items()
    print Cord.Items"""


def open_items():
    mouse_position(Cord.Item_cat_loc, True)
    left_click()
    time.sleep(1.0)


def close_items():
    mouse_position(Cord.Item_cat_loc, True)
    left_click()


def is_slot_empty_or_used(item):
    item_sum = get_pixel_sum_color(item, False)
    if item_sum >= 700000:  # empty
        return True
    else:
        return False


def is_item_available(item):
    open_items()
    result = is_slot_empty_or_used(item)
    close_items()
    return not result


def is_pot(pots, value):
    for pot in pots:
        if pot == value:
            return True
    return False


def have_item(item_type):
    for i in range(0, len(Cord.Items)):
        if Cord.Items[i] == item_type and is_item_available(Cord.ibox_list[i]) and Items.cool_down == 0:
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
    if current_health <= 50:
        if not is_item_active(0):
            if have_item(0):
                if use_item(0):
                    return True
    return False


def use_mana_pot(current_mana):
    if current_mana <= 70:
        if not is_item_active(1):
            if have_item(1):
                if use_item(1):
                    return True
    return False


def use_spirit_pot(current_spirit):
    if current_spirit <= 70:
        if not is_item_active(2):
            if have_item(2):
                if use_item(2):
                    return True
    return False


#0 = health, 1 = mana, 2 = spirit
def use_gem(gem_type, current):
    if gem_type == 0:
        if current <= 70 and Items.h_gem:
            activate_gem()
            Items.h_gem = False
            return True
    elif gem_type == 1:
        if current <= 70 and Items.m_gem:
            activate_gem()
            Items.m_gem = False
            return True
    elif gem_type == 2:
        if current <= 80 and Items.s_gem:
            activate_gem()
            Items.s_gem = False
            return True
    return False


def use_item(item_type):
    for i in range(0, len(Cord.Items)):
        if Cord.Items[i] == item_type and Items.cool_down[i] == 0:
            #Cord.Items[i] = 9 ##New Rule
            mouse_position(Cord.Item_cat_loc)
            left_click()
            mouse_position(Cord.item_locs[i])
            left_click()
            Items.cool_down[i] = Settings.cool_down
            return True
    logging.warning("No Items Could be Used.")
    return False