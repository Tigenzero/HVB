__author__ = 'Matt'
# TODO: Attack Enemy
# TODO: Use 3 different special attacks
# TODO:
import click_press


class AttackManager(object):
    def __init__(self, style, special_skills):
        """
        param style: single, dual, magic, niken
        """
        self.style = style
        self.special_skills = special_skills
        self.special_len = len(special_skills)
        self.attack_master = self.get_style(len(special_skills))

    def get_style(self, special_count):
        if self.style == 0:
            return DualMaster(special_count)


class _Base(object):
    def __init__(self, special_count):
        self.special_count = special_count
        self.overcharge = 0

    def attack(self, enemy_num):
        """
        uses string number "1" - "0" to attack enemy.
        enemy_num: string with value "1"-"0"
        """
        click_press.press(enemy_num)

    def _is_special_1_available(self, special_active, current_overcharge):
        if current_overcharge >= self.overcharge and special_active:
            pass
        else:
            return False

    def _is_special_2_available(self, special_active):
        if special_active:
            pass
        else:
            return

    def _is_special_3_available(self, special_active):
        if special_active:
            pass
        else:
            return

    def is_special_active(self, skill_list, special_num):
        for skill in skill_list:
            if skill.special == special_num:
                return skill.active
        return False


class DualMaster(_Base, ):

    def __init__(self, special_count):
        self.overcharge = 80

    def attack_enemies(self, skill_list, spirit_active, current_enemies, current_overcharge):
        """
        START HERE
        """
        attack_message = "Attacked Enemy"
        if spirit_active:
            self.attack(current_enemies[0])
            return attack_message
        special_3 = self.is_special_active(skill_list, 3)
        special_2 = self.is_special_active(skill_list, 2)

        special_num = get_active_special(skill_list)

        #if special 1 active and overcharge above rate, use
            #special 1 is 'special' because the overcharge requirement changes based on how many specials the player has

    def get_active_special(self, skill_list, current_enemies):
        if self.is_special_active(skill_list, 3):
            self.special_attack(current_enemies, 3)
        elif self.is_special_active(skill_list, 2):
            self.special_attack(current_enemies, 2)
        elif self.is_special_active(skill_list, 1) and :


    def special_attack(self, enemy_list, special_num):

