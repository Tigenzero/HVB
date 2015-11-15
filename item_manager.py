import logging
import Click_Press
from Coordinates import ItemCords
import Settings
import time


class Item(object):
    """
    Item class: object representing a single item
    type: health, mana, spirit
    level: potency of the item and how long the cool down lasts
    """
    def __init__(self, i_type, coordinates):
        self.type = i_type
        self.cool_down = 0
        self.available = True
        self.coordinates = coordinates

    def cool_down(self):
        if self.available:
            return
        self.cool_down -= 1
        if self.cool_down <= 0:
            self.available = True


class ItemManager(object):
    def __init__(self):
        self.current_gem = None
        self.item_cords = ItemCords()
        self.items = []

    def get_items(self):
        for index, item in enumerate(list(Settings.Player.items)):
            self.items[index] = Item(item, self.item_cords.item_locs[index])

    def use_item(self, item):
        if not item.available:
            logging.critical("Item cannot be used if it is unavailable.")
        Click_Press.mousePos(self.item_cords.item_cat_loc)
        Click_Press.leftClick()
        Click_Press.mousePos(item.coordinates)
        Click_Press.leftClick()
        item.cool_down = 20  # Fix Later as a cool down dictionary that checks levels

    def cool_down_items(self):
        for item in self.items:
            item.cool_down()

    def activate_gem(self):
        self.open_items()
        Click_Press.mousePos(self.item_cords.gem_loc)
        Click_Press.leftClick()

    def open_items(self):
        Click_Press.mousePos(self.item_cords.item_cat_loc, True)
        Click_Press.leftClick()
        time.sleep(1.0)

    def _close_items(self):
        Click_Press.mousePos(self.item_cords.item_cat_loc, True)
        Click_Press.leftClick()

    def get_gem(self, gem_color):
        """
        :param gem_color: result of Status.get_pixel_sum_color(self.item_cords.ibox_gem)
        :return: logging message
        """
        message = "no gem found"
        if 710000 <= gem_color <= 719999:
            #logging.debug("health gem found")
            message = "health gem found"
            self.current_gem = 0
        elif 729000 <= gem_color <= 729999:
            #logging.debug("mana gem found")
            message = "mana gem found"
            self.current_gem = 1
        elif 723000 <= gem_color <= 723999:
            #logging.debug("spirit gem found")
            message = "spirit gem found"
            self.current_gem = 2
        elif 722000 <= gem_color <= 722999:
            self.current_gem = 3
            message = "Channeling gem found"
        Click_Press.mousePos(self.item_cords.item_cat_loc)
        Click_Press.leftClick()
        return message
