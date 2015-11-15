import pony_watcher
import find_window


def test_is_pony_time_init():
    image = open("test_window.png").convert('RBG')
    watcher = pony_watcher.PonyWatcher()


