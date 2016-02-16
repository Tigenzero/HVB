__author__ = 'Matt'
"""
EXECUTE FROM PROJECT ROOT
To Execute:python -m nose -v skill/live_tests/test_skill_manager_live.py
"""

from nose.tools import raises

from skill.skill_manager import SkillGenerator, SkillMonitor
from player.player_config import PlayerConfig
import window_finder.find_window
import window_finder.scanner

window_grabber = window_finder.find_window.ScreenGrabber.get_window()


@raises(IOError)
def test_skill_skill_manager_live_skill_monitor():
    window_grabber.refresh_image()
    image = window_grabber.image
    player_config = PlayerConfig()
    player_config.get_player_config()
    player = player_config.player_list[0]
    skill_gen = SkillGenerator.generate_skills(player.skills, player.premium, player.special)
    skills = SkillMonitor.update_skills(image, skill_gen)
    for skill in skills:
        skill.print_skill()
