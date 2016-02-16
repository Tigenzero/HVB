"""
skill_manager manages everything skill related:
obtaining skill images
holding skill hotkey bounding box coordinates
holding skill button click locations
holding the current active and inactive skill objects
"""

import logging

from Settings import Settings


# TODO: Add Attack Master
# TODO: Add Premium Skill Use / Uses
from status import image_initialize
from user_interface import coordinates, click_press, etc_manager


class Skill(object):
    """
    Every Attribute of a Skill in a single class
    self.name = string
    self.active = bool
    self.click_coordinates = (int, int)
    self.box_bounds = (int, int, int, int)
    self.premium = bool
    self.special = int
    """
    def __init__(self, name, active, click_coordinates, box_bounds, premium, special=0):
        self.name = name
        self.active = active
        self.click_coordinates = click_coordinates
        self.box_bounds = box_bounds
        self.premium = premium
        self.special = special

    def use_skill(self):
        click_press.mouse_position(self.click_coordinates)
        click_press.left_click()

    def print_skill(self):
        logging.info("Name: {}".format(self.name))
        logging.info("Active: {}".format(self.active))
        logging.info("Premium: {}".format(self.premium))
        logging.info("Special: {}".format(self.special))


class SkillGenerator(object):
    """
    Gets Player skill names, skill coordinates, skill bounding boxes, and generates a list of skills
    """
    def __init__(self, player_skill_names, player_premium_slots, player_special_slots):
        self.skill_cords = coordinates.SkillHKCords()
        self.skill_names = player_skill_names
        self.premium_slots = player_premium_slots
        self.special_slots = player_special_slots
        if not type(self.skill_names) is list:
            raise ValueError("Player skill names not of type list")
        if not type(self.premium_slots) is list:
            raise ValueError("Player premium slots not of type list")
        if not type(self.special_slots) is list:
            raise ValueError("Player special slots not of type list")

    @staticmethod
    def _create_skill(name, click_coord, box_bounds, active=True, premium=False, special=0):
        return Skill(name, active, click_coord, box_bounds, premium, special)

    def _is_skill_premium(self, name):
        return name in self.premium_slots

    def _is_skill_special(self, index):
        return index in self.special_slots

    @staticmethod
    def _is_invalid_skill_name(name):
        return name == "Empty" or name == "None"

    def _get_special_num(self, index):
        for spec_index, spec_num in enumerate(self.special_slots):
            if spec_num == index:
                return spec_index + 1

    @classmethod
    def generate_skills(cls, player_skill_names, player_premium_slots, player_special_slots):
        skill_gen = cls(player_skill_names, player_premium_slots, player_special_slots)
        skill_list = []
        for index in range(0, len(skill_gen.skill_names) - 1):
            name = player_skill_names[index]
            if skill_gen._is_invalid_skill_name(name):
                logging.warning("Skill is Invalid, ignoring: {}".format(name))
                continue
            loc = skill_gen.skill_cords.skill_locs[index]
            box_bounds = skill_gen.skill_cords.skill_box_locs[index]
            is_premium = skill_gen._is_skill_premium(name)
            special = skill_gen._is_skill_special(index)
            special_num = 0
            if special:
                special_num = skill_gen._get_special_num(index)
            skill = skill_gen._create_skill(name, loc, box_bounds, active=True, premium=is_premium, special=special_num)
            skill_list.append(skill)
            logging.debug(skill.name)
        return skill_list


class SkillMonitor(object):
    """
    Obtains up to date skill information
    """
    def __init__(self):
        self.active_skill_collection, self.inactive_skill_collection = image_initialize.get_skill_images()
        self.skill_kill = False

    def _is_skill_sum_active(self, skill_sum):
        return self.active_skill_collection.get(skill_sum) is not None

    def _is_skill_sum_inactive(self, skill_sum):
        return self.inactive_skill_collection.get(skill_sum) is not None

    def _skill_sum_buffer(self, pixel_sum, active=True):
        logging.info("Skill Buffer Being Used")
        if active:
            collection = self.active_skill_collection
        else:
            collection = self.inactive_skill_collection

        for key, value in collection.items():
            if key - Settings.skill_buffer <= pixel_sum <= key + Settings.skill_buffer:
                logging.debug("Skill sum {} is {} away from {} which is {}".format(pixel_sum,
                                                                                   Settings.skill_buffer,
                                                                                   key,
                                                                                   value))
                return value
        return None

    def print_active_skill_collection(self):
        image_initialize.print_collection(self.active_skill_collection)

    def print_inactive_skill_collection(self):
        image_initialize.print_collection(self.inactive_skill_collection)

    @staticmethod
    def _get_skill_sum(image, box_bounds):
        return etc_manager.get_pixel_sum_color(image, box_bounds)

    def _is_skill_active_buffer(self, skill, image):
        skill_sum = self._get_skill_sum(image, skill.box_bounds)
        result = self._skill_sum_buffer(skill_sum, True)
        if result is not None:
            self.active_skill_collection[skill_sum] = result
            return True
        result2 = self._skill_sum_buffer(skill_sum, False)
        if result2 is not None:
            self.inactive_skill_collection[skill_sum] = result2
            return False
        else:
            logging.critical("UNKNOWN skill: %d" % skill_sum)
            etc_manager.get_pixel_sum_color(image, skill.box_bounds)
            self.skill_kill = True
            return None

    def _is_skill_active(self, skill, image):
        skill_sum = self._get_skill_sum(image, skill.box_bounds)
        logging.debug("{}: {}".format(skill.name, skill_sum))
        if self._is_skill_sum_active(skill_sum):
            return True
        elif self._is_skill_sum_inactive(skill_sum):
            return False
        else:
            return self._is_skill_active_buffer(skill, image)

    @classmethod
    def update_skills(cls, image, skill_list):
        monitor = cls()
        for skill in skill_list:
            skill.active = monitor._is_skill_active(skill, image)
        if monitor.skill_kill:
            logging.critical("Not all skills were identified. Shutting down now.")
            quit()
        return skill_list


class SpiritMaster(object):
    """
    SpiritMaster manages the use and monitoring of Spirit
    """
    def __init__(self):
        self.overcharge_cooldown = 0
        self.spirit_cords = coordinates.SpiritCords()
        self.overcharge_max = 80

    def _is_spirit_possible(self, current_overcharge, current_spirit):
        if current_overcharge >= self.overcharge_max and self.overcharge_cooldown == 0 and current_spirit >= 40 \
                and Settings.Player.spirit:
            pass
        else:
            return False

    def _is_spirit_active(self, image):
        if image.getpixel(self.spirit_cords.spirit_cat_loc) == self.spirit_cords.spirit_active_color:
            return True
        else:
            return False

    def _spirit_cooldown(self):
        if self.overcharge_cooldown > 0:
            self.overcharge_cooldown -= 1

    def is_spirit_available(self, image, current_overcharge, current_spirit):
        if self._is_spirit_active(image) and self._is_spirit_possible(current_overcharge, current_spirit):
            pass
        else:
            return False

    def use_spirit(self):
        click_press.mouse_position(self.spirit_cords.spirit_cat_loc)
        click_press.left_click()
        self.overcharge_cooldown = 10


class SkillMaster(object):
    """
    Obtains skills from SkillGenerator
    Updates skills' active states
    Updates and uses spirit
    """
    def __init__(self, skill_list):

        self.current_skills = skill_list
        self.skill_monitor = SkillMonitor()
        self.spirit_master = SpiritMaster()

    def update_skills(self, image):
        self.spirit_master._spirit_cooldown()
        self.current_skills = self.skill_monitor.update_skills(image, self.current_skills)

    def is_spirit_available(self, image, current_overcharge, current_spirit):
        return self.spirit_master.is_spirit_available(image, current_overcharge, current_spirit)

    def is_spirit_active(self, image):
        return self.spirit_master._is_spirit_active(image)

    def use_spirit(self):
        self.spirit_master.use_spirit()

    def use_skill(self, skill_name):
        for skill in self.current_skills:
            if skill.name == skill_name:
                skill.use_skill()

    def get_skill(self, skill_name):
        for skill in self.current_skills:
            if skill.name == skill_name:
                return skill
