from player import player_monitor
import Image
import logging

PLAYER_HP_70 = Image.open("player/tests/data/HV_player_hp_50.jpg").convert("RGB")


def test_player_monitor_init():
    player_monitor.PlayerMonitor()


def test_player_monitor_refresh_stats_health_70():
    monitor = player_monitor.PlayerMonitor()
    monitor.refresh_stats(PLAYER_HP_70)
    logging.debug("Health: {}".format(monitor.health))
    logging.debug("Mana: {}".format(monitor.mana))
    logging.debug("Spirit: {}".format(monitor.spirit))
    logging.debug("Overcharge: {}".format(monitor.overcharge))
    assert(monitor.health == 70)
    assert(monitor.mana == 100)
    assert(monitor.spirit == 100)
    assert(monitor.overcharge == 100)