import os
import logging

from PIL import Image

from window_finder import find_window, scanner


TEST_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "test_full_window.png")
SCANNER_RESULT = (120, 225)
TEST_DIMENSIONS = [1357, 831]
WINDOW_GRABBER = find_window.ScreenGrabber()
WINDOW_GRABBER.image = Image.open(TEST_IMAGE)
WINDOW_GRABBER.image.convert('RGB')
# 1920X1080

WINDOW_GRABBER.screen_height = TEST_DIMENSIONS[1]
WINDOW_GRABBER.screen_width = TEST_DIMENSIONS[0]
WINDOW_GRABBER.window_dimensions = [0, 0, TEST_DIMENSIONS[0], TEST_DIMENSIONS[1]]


def test_screen_grabber_init():
    find_window.ScreenGrabber()
    pass


def test_find_window_screen_grabber_find_left():
    left = WINDOW_GRABBER.find_left(SCANNER_RESULT)
    logging.info("left: {}".format(left))
    assert(left == 42)


def test_find_window_screen_grabber_find_top():
    top = WINDOW_GRABBER.find_top(42, SCANNER_RESULT[1])
    logging.info("top: {}".format(top))
    assert(top == 102)


def test_find_window_corner():
    window = scanner.Scanner.run(WINDOW_GRABBER.screen_width,
                                 WINDOW_GRABBER.screen_height,
                                 WINDOW_GRABBER.scan_size,
                                 WINDOW_GRABBER.image,
                                 find_window.WINDOW_COLORS)
    left = WINDOW_GRABBER.find_left(window)
    top = WINDOW_GRABBER.find_top(left, window[1])
    logging.info("x:{} y:{}".format(top, left))
    assert(left == 42)
    assert(top == 102)


def test_find_window_dimensions():
    window = scanner.Scanner.run(WINDOW_GRABBER.screen_width,
                                 WINDOW_GRABBER.screen_height,
                                 WINDOW_GRABBER.scan_size,
                                 WINDOW_GRABBER.image,
                                 find_window.WINDOW_COLORS)
    left = WINDOW_GRABBER.find_left(window)
    top = WINDOW_GRABBER.find_top(left, window[1])
    WINDOW_GRABBER.window_dimensions = (left, top, left + 1235, top + 720)
    logging.info(WINDOW_GRABBER.window_dimensions)
    assert (WINDOW_GRABBER.window_dimensions == (42, 102, 1277, 822))


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