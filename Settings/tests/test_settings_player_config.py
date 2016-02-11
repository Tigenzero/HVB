__author__ = 'Matt'
from Settings.player_config import PlayerConfig
import os

SKILLS = "Cure,Haste,Special,Special,Special"
SETTINGS_FILE = os.path.join("data", "Player.txt")


def test_settings_player_config_init():
    PlayerConfig()


def test_settings_player_config_get_skills():
    player_config = PlayerConfig()
    skills = player_config._get_skills(SKILLS)
    assert(skills == ["Cure", "Haste", "Special", "Special", "Special"])


def test_settings_player_config_get_spirit_true():
    player_config = PlayerConfig()
    spirit = player_config._get_spirit("True")
    assert spirit


def test_settings_player_config_get_spirit_false():
    player_config = PlayerConfig()
    spirit = player_config._get_spirit("False")
    assert not spirit


def test_settings_player_config_get_player_config():
    player_config = PlayerConfig()
    player_config.get_player_config()
    player = player_config.player_list[0]
    assert(len(player_config.player_list) == 1)
    assert(player.skills == ['Cure', 'Regen', 'Heartseeker', 'Spirit_Shield', 'Absorb', 'Special', 'Special', 'Special', 'Blind', 'Drain', 'Weaken', 'Sleep', 'Spark_Life', 'Empty', 'Empty', 'Empty'])
    assert(player.items == (0, 0, 0, 1, 1, 2, 2, 9, 9, 9, 9, 9, 9, 9, 9, 9))
    assert(player.name == "Player_0")
    assert(player.premium == ['Heartseeker', 'Spark_Life', 'Spirit_Shield', 'Haste'])
    assert(player.style == 0)
    assert(player.name == "Player_0")
    assert(player.max_sleep == 0.0)
    assert(player.min_sleep == 0.0)
    assert not player.spirit
    assert(player.special == [5, 6, 7])