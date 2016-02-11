__author__ = 'Matt'
#TODO: Finish Tests Listed at Bottom
import os
from skill.skill_manager import SkillMonitor, SkillGenerator
import window_finder.find_window
import logging
from PIL import Image

TEST_IMAGE = Image.open(os.path.join("skill", "tests", "data", "test_full_window.png")).convert("RGB")
PREMIUM = ['Heartseeker', 'Spark_Life', 'Spirit_Shield', 'Haste']
SKILLS = ['Cure', 'Regen', 'Heartseeker', 'Spirit_Shield', 'Absorb', 'Special', 'Special', 'Special', 'Blind', 'Drain', 'Weaken', 'Sleep', 'Spark_Life', 'Empty', 'Empty', 'Empty']
SPECIAL = [5, 6, 7]
WINDOW_GRABBER = window_finder.find_window.ScreenGrabber.get_window_test(TEST_IMAGE)
SKILL_LIST = SkillGenerator.generate_skills(SKILLS, PREMIUM, SPECIAL)
CURE_ACTIVE_SUM = 192171
SPECIAL_INACTIVE_SUM = 508737


def test_skill_skill_manager_skill_monitor_init():
    SkillMonitor()
    pass


def test_skill_skill_manager_skill_monitor_get_skill_sum():
    skill_monitor = SkillMonitor()
    skill_bound_box = SKILL_LIST[0].box_bounds
    skill_sum = skill_monitor._get_skill_sum(WINDOW_GRABBER.image, skill_bound_box)
    logging.debug("Cure: {}".format(skill_sum))
    assert(skill_sum == CURE_ACTIVE_SUM)


def test_skill_skill_manager_skill_monitor_is_skill_sum_active_true():
    skill_monitor = SkillMonitor()
    result = skill_monitor._is_skill_sum_active(CURE_ACTIVE_SUM)
    skill_monitor.print_active_skill_collection()
    logging.debug("active skill collection result: {}".format(result))
    assert result


def test_skill_skill_manager_skill_monitor_is_skill_sum_active_false():
    skill_monitor = SkillMonitor()
    result = skill_monitor._is_skill_sum_active(SPECIAL_INACTIVE_SUM)
    skill_monitor.print_active_skill_collection()
    logging.debug("active skill collection result: {}".format(result))
    assert result is False


def test_skill_skill_manager_skill_monitor_is_skill_sum_inactive_false():
    skill_monitor = SkillMonitor()
    result = skill_monitor._is_skill_sum_inactive(CURE_ACTIVE_SUM)
    skill_monitor.print_active_skill_collection()
    logging.debug("inactive skill collection result: {}".format(result))
    assert result is False


def test_skill_skill_manager_skill_monitor_is_skill_sum_inactive_true():
    skill_monitor = SkillMonitor()
    result = skill_monitor._is_skill_sum_inactive(SPECIAL_INACTIVE_SUM)
    skill_monitor.print_inactive_skill_collection()
    logging.debug("inactive skill collection result: {}".format(result))
    assert result

#test_skill_skill_manager_skill_monitor_is_skill_active_false

#test_skill_skill_manager_skill_monitor_is_skill_active_true

#test_skill_skill_manager_skill_monitor_is_skill_active_buffer_true

#test_skill_skill_manager_skill_monitor_is_skill_active_buffer_false

#test_skill_skill_manager_skill_monitor_skill_sum_buffer_not_None

#test_skill_skill_manager_skill_monitor_skill_sum_buffer_None

#test_skill_skill_manager_skill_monitor_update_skills