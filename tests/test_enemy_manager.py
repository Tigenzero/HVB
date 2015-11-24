import enemy_monitor
import os
from PIL import Image

TEST_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_HV_window.png")


def test_enemy_monitor_init():
    enemy_monitor.EnemyMonitor()


def test_enemy_monitor_get_enemies():
    image = Image.open(TEST_IMAGE)
    image.convert('RGB')
    e_m = enemy_monitor.EnemyMonitor()
    e_m.get_enemies(image)
    assert(e_m.enemy_count == 1)