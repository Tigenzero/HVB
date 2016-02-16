__author__ = 'Matt'
import os
import logging

import Image

from skill.attack_manager import AttackManager
from player.player_config import PlayerConfig
from skill.skill_manager import SkillGenerator
from window_finder import find_window
from Settings import Settings


PLAYER = PlayerConfig.get_player_0()
SKILL_LIST = SkillGenerator.generate_skills(PLAYER.skills,
                                            PLAYER.premium,
                                            PLAYER.special)
TEST_IMAGE = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "test_full_window.png")).convert('RGB')

WINDOW = find_window.ScreenGrabber.get_window_test(TEST_IMAGE)

def test_skill_attack_manager_init():
    AttackManager(0)


def test_skill_attack_manager_parse_special():
    attack_manager = AttackManager(0)
    attack_manager.parse_special(SKILL_LIST)
    assert(attack_manager.special_len == 3)
    for skill in attack_manager.special_skills:
        assert(skill.special > 0)


def test_skill_attack_manager_get_style():
    attack_manager = AttackManager(0)
    assert(attack_manager.get_style(3).overcharge == 80)


def test_skill_attack_manager_attack_enemies_special_1_pass():
    Settings.box = WINDOW.window_dimensions
    for skill in SKILL_LIST:
        if skill.special == 1:
            skill.active = True
        else:
            skill.active = False
    attack_manager = AttackManager(0)
    current_enemies = ["0", "1", "2"]
    attack_result = attack_manager.attack_master.attack_enemies(SKILL_LIST, False, current_enemies, 80)
    logging.debug("attack_result: {}".format(attack_result))
    assert(attack_result == "Attacked Enemy 0 with Special 1")


def test_skill_attack_manager_attack_enemies_special_2_pass():
    Settings.box = WINDOW.window_dimensions
    for skill in SKILL_LIST:
        if skill.special == 1 or skill.special == 2:
            skill.active = True
        else:
            skill.active = False
    attack_manager = AttackManager(0)
    current_enemies = ["0", "1", "2"]
    attack_result = attack_manager.attack_master.attack_enemies(SKILL_LIST, False, current_enemies, 80)
    logging.debug("attack_result: {}".format(attack_result))
    assert(attack_result == "Attacked Enemy 0 with Special 2")


def test_skill_attack_manager_attack_enemies_special_3_3_enemies_pass():
    Settings.box = WINDOW.window_dimensions
    for skill in SKILL_LIST:
            skill.active = True
    attack_manager = AttackManager(0)
    current_enemies = ["0", "1", "2"]
    attack_result = attack_manager.attack_master.attack_enemies(SKILL_LIST, False, current_enemies, 80)
    logging.debug("attack_result: {}".format(attack_result))
    assert(attack_result == "Attacked Enemy 1 with Special 3")


def test_skill_attack_manager_attack_enemies_special_3_1_enemy_pass():
    Settings.box = WINDOW.window_dimensions
    for skill in SKILL_LIST:
            skill.active = True
    attack_manager = AttackManager(0)
    current_enemies = ["0"]
    attack_result = attack_manager.attack_master.attack_enemies(SKILL_LIST, False, current_enemies, 80)
    logging.debug("attack_result: {}".format(attack_result))
    assert(attack_result == "Attacked Enemy 0 with Special 3")


def test_skill_attack_manager_attack_enemies_spirit_active_pass():
    Settings.box = WINDOW.window_dimensions
    for skill in SKILL_LIST:
            skill.active = True
    attack_manager = AttackManager(0)
    current_enemies = ["0"]
    attack_result = attack_manager.attack_master.attack_enemies(SKILL_LIST, True, current_enemies, 80)
    logging.debug("attack_result: {}".format(attack_result))
    assert(attack_result == "Attacked Enemy 0")


def test_skill_attack_manager_attack_enemies_no_special_pass():
    Settings.box = WINDOW.window_dimensions
    for skill in SKILL_LIST:
            skill.active = False
    attack_manager = AttackManager(0)
    current_enemies = ["0", "1", "2"]
    attack_result = attack_manager.attack_master.attack_enemies(SKILL_LIST, False, current_enemies, 80)
    logging.debug("attack_result: {}".format(attack_result))
    assert(attack_result == "Attacked Enemy 0")


def test_skill_attack_manager_find_mid_enemy_3():
    attack_manager = AttackManager(0)
    enemies = ["0", "1", "2"]
    mid_enemy = attack_manager.attack_master.find_mid_enemy(enemies)
    assert(mid_enemy == "1")


def test_skill_attack_manager_find_mid_enemy_5():
    attack_manager = AttackManager(0)
    enemies = ["0", "1", "2", "3", "4"]
    mid_enemy = attack_manager.attack_master.find_mid_enemy(enemies)
    assert(mid_enemy == "2")

