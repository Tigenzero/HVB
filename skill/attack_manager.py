from user_interface import click_press

__author__ = 'Matt'
# TODO: Attack Enemy
# TODO: Use 3 different special attacks
# TODO:
import logging


class AttackManager(object):
    """
    Purpose of AttackManager is to manage the attack style of the player
    and the special skills available to attack enemies
    param style: style of attack (examples: single (1), dual (0), magic (2), niken (3)
    param special_skills: list of skills and their details
    """
    def __init__(self, style):
        self.style = style
        self.special_skills = None
        self.special_len = None
        self.attack_master = self.get_style(style)

    def get_style(self, special_count):
        if self.style == 0:
            return DualMaster(special_count)
        elif self.style == 1:
            logging.critical("The One-Handed attack style has not been implemented yet")
            return None
        elif self.style == 2:
            logging.critical("The Magic attack style has not been implemented yet")
            return None
        elif self.style == 3:
            logging.critical("The Niken attack style has not been implemented yet")
            return None


class _Base(object):
    def __init__(self, special_count):
        self.special_count = special_count
        self.overcharge = None

    @staticmethod
    def attack(enemy_key):
        """
        uses string number "1" - "0" to attack enemy.
        enemy_key: string with value "1"-"0"
        """
        logging.debug("Enemy Attacked: pressed ".format(enemy_key))
        click_press.press(enemy_key)

    def _is_special_1_available(self, special_active, current_overcharge):
        if current_overcharge >= self.overcharge and special_active:
            pass
        else:
            return False

    @staticmethod
    def _is_special_2_available(special_active):
        if special_active:
            pass
        else:
            return

    @staticmethod
    def _is_special_3_available(special_active):
        if special_active:
            pass
        else:
            return

    @staticmethod
    def is_special_active(skill_list, special_num):
        for skill in skill_list:
            if skill.special == special_num:
                return skill.active
        return False

    @staticmethod
    def parse_specials(skill_list):
        special_1 = None
        special_2 = None
        special_3 = None
        for skill in skill_list:
            if skill.special == 3:
                special_3 = skill
            elif skill.special == 2:
                special_2 = skill
            elif skill.special == 1:
                special_1 = skill
        return special_1, special_2, special_3


class DualMaster(_Base):
    def __init__(self, special_count):
        super(DualMaster, self).__init__(special_count)
        self.overcharge = 80

    def attack_enemies(self, skill_list, spirit_active, current_enemies, current_overcharge):
        """
        uses current specials at disposial to attack enemies
        param skill_list: list of skill objects
        param spirit_active: status of the spirit power
        param current_enemies: list of living enemies
        param current_overcharge: percentage of overcharge that is filled
        """
        if len(current_enemies) == 0:
            return "No enemies in Attack Phase. Returning"
        attack_message = "Attacked Enemy {}".format(current_enemies[0])
        if spirit_active:
            self.attack(current_enemies[0])
            return attack_message
        special_1, special_2, special_3 = self.parse_specials(skill_list)
        if self.activate_special(special_3):
            special_3.use_skill()
            mid_enemy = self.find_mid_enemy(current_enemies)
            self.attack(mid_enemy)
            attack_message = "Attacked Enemy {} with Special 3".format(mid_enemy)
        elif self.activate_special(special_2):
            special_2.use_skill()
            self.attack(current_enemies[0])
            attack_message = "Attacked Enemy {} with Special 2".format(current_enemies[0])
        elif self.activate_special(special_1) and current_overcharge >= self.overcharge:
            special_1.use_skill()
            self.attack(current_enemies[0])
            attack_message = "Attacked Enemy {} with Special 1".format(current_enemies[0])
        else:
            self.attack(current_enemies[0])
        return attack_message

    @staticmethod
    def find_mid_enemy(enemies):
        if type(enemies) is not list:
            logging.debug(enemies)
            logging.debug("enemies is not list, returning")
            return enemies
        enemy_len = len(enemies)
        mid_enemy = int(enemy_len/2)
        logging.debug("Enemy Length: {}".format(enemies))
        logging.debug("Mid Enemy: {}".format(mid_enemy))
        return enemies[mid_enemy]

    @staticmethod
    def activate_special(special):
        if special is not None and special.active:
            return True
        return False