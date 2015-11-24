import os
import find_window
from PIL import Image
import scanner
import logging

TEST_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_full_window.png")


def test_screen_grabber_init():
    find_window.ScreenGrabber()
    pass


def test_find_window_corner():
    window_grabber = find_window.ScreenGrabber()
    window_grabber.image = Image.open(TEST_IMAGE)
    window_grabber.image.convert('RGB')
    x, y = scanner.Scanner.run(window_grabber.screen_width,
                               window_grabber.screen_height,
                               window_grabber.scan_size,
                               window_grabber.image,
                               find_window.WINDOW_COLORS)
    logging.info("x:{} y:{}".format(x, y))


def test_find_window_dimensions():
    window_grabber = find_window.ScreenGrabber()
    window_grabber.image = Image.open(TEST_IMAGE)
    window_grabber.image.convert('RGB')
    window = scanner.Scanner.run(window_grabber.screen_width,
                                 window_grabber.screen_height,
                                 window_grabber.scan_size,
                                 window_grabber.image,
                                 find_window.WINDOW_COLORS)
    left = window_grabber.find_left(window)
    top = window_grabber.find_top(left, window[1])
    window_grabber.window_dimensions = (left, top, left + 1235, top + 720)
    logging.info(window_grabber.window_dimensions)


"""def test_find_window_save_small_window():
    window_grabber = find_window.ScreenGrabber()
    window_grabber.image = Image.open(TEST_IMAGE)
    window_grabber.refresh_image()
    window = scanner.Scanner.run(window_grabber.screen_width,
                                 window_grabber.screen_height,
                                 window_grabber.scan_size,
                                 window_grabber.image,
                                 find_window.WINDOW_COLORS)
    left = window_grabber.find_left(window)
    top = window_grabber.find_top(left, window[1])
    window_grabber.window_dimensions = (left, top, left + 1235, top + 720)
    window_grabber.refresh_image()
    window_grabber.save()"""