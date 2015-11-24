"""
skill_manager manages everything skill related:
obtaining skill images
holding skill hotkey bounding box coordinates
holding skill button click locations
holding the current active and inactive skill objects
"""

import image_initialize
import coordinates
import logging
import Settings
import etc_manager
import click_press

# TODO: Add Use Skills, Add Attack Enemies


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

    def _create_skill(self, name, click_coord, box_bounds, active=True, premium=False, special=0):
        return Skill(name, active, click_coord, box_bounds, premium, special)

    def _is_skill_premium(self, name):
        return name in self.premium_slots

    def _is_skill_special(self, index):
        return index in self.special_slots

    def _is_invalid_skill_name(self, name):
        return name != "Empty" and name != "None"

    @classmethod
    def generate_skills(cls, player_skill_names, player_premium_slots, player_special_slots):
        skill_gen = cls(player_skill_names, player_premium_slots, player_special_slots)
        skill_list = []
        for index in range(0, len(skill_gen.skill_names) - 1):
            name = player_skill_names[index]
            if skill_gen._is_invalid_skill_name(name):
                continue
            loc = skill_gen.skill_cords.skill_locs[index]
            box_bounds = skill_gen.skill_cords.skill_box_locs[index]
            is_premium = skill_gen._is_skill_premium(name)
            special_num = skill_gen._is_skill_special(index)
            skill = skill_gen._create_skill(name, loc, box_bounds, is_premium, special_num)
            skill_list.append(skill)
        return skill_list





class SkillMonitor(object):
    """
    Obtains up to date skill information
    """
    def __init__(self):
        self.active_skill_collection, self.inactive_skill_collection = image_initialize.get_skill_images()

    def get_skills(self, image):
        skill_count = 0
        skill_kill = False
        for skill in self.skill_cords.skill_box_locs:
            #sum = get_pixel_sum_color(skill)
            sum = etc_manager.get_pixel_sum_color(image, skill)
            logging.debug("Skill {}: {}".format(skill_count, sum))

            result = self.active_skill_collection.get(sum)
            result2 = self.inactive_skill_collection.get(sum)
            if result is not None:
                self.current_skills[skill_count] = result
            elif result2 is not None:
                self.current_skills[skill_count] = result2
            else:
                result = self.skill_sum_buffer(sum, True)
                if result is not None:
                    self.current_skills[skill_count] = result
                    self.active_skill_collection[sum] = result
                else:
                    result2 = self.skill_sum_buffer(sum, False)
                    if result2 is not None:
                        self.current_skills[skill_count] = result2
                        self.inactive_skill_collection[sum] = result2
                    else:
                        logging.warning("UNKNOWN skill: %d" % sum)
                        etc_manager.get_pixel_sum_color(image, skill)
                        skill_kill = True
            skill_count += 1
        if skill_kill:
            logging.critical("Not all skills were identified. Shutting down now.")
            quit()

    def _is_skill_sum_active(self, skill_sum):
        return self.active_skill_collection.get(skill_sum) is None

    def _is_skill_sum_inactive(self, skill_sum):
        return self.inactive_skill_collection.get(skill_sum) is None


class SkillMaster(object):
    """

    """
    def __init__(self):

        self.current_skills = []
        self.overcharge_cooldown = 0



    def skill_sum_buffer(self, pixel_sum, active=True):
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

    def use_skill(self, skill):
        #mouse_position(Cord.Cure)
        if skill >= 0:
            click_press.mouse_position(self.skill_cords.skill_locs[skill])
            click_press.left_click()

    def use_spirit(self, image, current_spirit, current_overcharge):
        if current_overcharge >= 80 and self.overcharge_cooldown <= 0 and current_spirit >= 40 \
                and not self._is_spirit_active(image) and Settings.Player.spirit:
            click_press.mouse_position(self.skill_cords.spirit_cat_loc)
            click_press.left_click()
            self.overcharge_cooldown = 10
            return True
        else:
            self.overcharge_cooldown -= 1
            return False

    def _is_spirit_active(self, image):
        if image.getpixel(self.skill_cords.spirit_cat_loc) == self.skill_cords.spirit_active_color:
            return True
        else:
            return False
