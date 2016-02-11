import logging
import click_press
from coordinates import ItemCords
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
    def __init__(self, player_items):
        self.player_items = player_items
        self.current_gem = None
        self.item_cords = ItemCords()
        self.items = []
        self.h_available = True
        self.m_available = True
        self.s_available = True
        self.next_h = None
        self.next_m = None
        self.next_s = None

    def get_items(self):
        for index, item in enumerate(list(self.player_items)):
            self.items[index] = Item(item, self.item_cords.item_locs[index])
            self.check_inventory()

    def use_item(self, item):
        if not item.available:
            logging.critical("Item cannot be used if it is unavailable.")
        click_press.mouse_position(self.item_cords.item_cat_loc)
        click_press.left_click()
        click_press.mouse_position(item.coordinates)
        click_press.left_click()
        item.cool_down = 20  # Fix Later as a cool down dictionary that checks levels
        item.available = False
        # BE SURE TO SET ITEM'S SOURCE SELF.NEXT_# TO NONE

    def cool_down_items(self):
        for item in self.items:
            item.cool_down()

    def activate_gem(self):
        self.open_item_tab()
        click_press.mouse_position(self.item_cords.gem_loc)
        click_press.left_click()

    def open_item_tab(self):
        click_press.mouse_position(self.item_cords.item_cat_loc, True)
        click_press.left_click()
        time.sleep(1.0)

    def close_item_tab(self):
        click_press.mouse_position(self.item_cords.item_cat_loc, True)
        click_press.left_click()

    def get_gem(self, gem_color):
        """
        :param gem_color: result of status.get_pixel_sum_color(self.item_cords.ibox_gem)
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
        click_press.mouse_position(self.item_cords.item_cat_loc)
        click_press.left_click()
        return message

    def check_inventory(self):
        self.h_available = False
        self.m_available = False
        self.s_available = False
        for item in self.items:
            if item.available is not True:
                continue
            if item.type == 0:
                self.h_available = True
            elif item.type == 1:
                self.m_available = True
            elif item.type == 1:
                self.s_available = True
            if self.next_h is None and item.type == 0:
                self.next_h = item
            elif self.next_m is None and item.type == 1:
                self.next_m = item
            elif self.next_s is None and item.type == 2:
                self.next_s = item
