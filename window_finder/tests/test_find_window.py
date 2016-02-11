import os
import logging

from PIL import Image

from window_finder import find_window, scanner


TEST_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "test_full_window.png")
SCANNER_RESULT = (120, 225)


def test_screen_grabber_init():
    find_window.ScreenGrabber()
    pass


def test_find_window_screen_grabber_find_left():
    window_grabber = find_window.ScreenGrabber()
    window_grabber.image = Image.open(TEST_IMAGE)
    window_grabber.image.convert('RGB')
    left = window_grabber.find_left(SCANNER_RESULT)
    logging.info("left: {}".format(left))
    assert(left == 42)


def test_find_window_screen_grabber_find_top():
    window_grabber = find_window.ScreenGrabber()
    window_grabber.image = Image.open(TEST_IMAGE)
    window_grabber.image.convert('RGB')
    top = window_grabber.find_top(42, SCANNER_RESULT[1])
    logging.info("top: {}".format(top))
    assert(top == 102)


def test_find_window_corner():
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
    logging.info("x:{} y:{}".format(top, left))
    assert(left == 42)
    assert(top == 102)


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
    assert (window_grabber.window_dimensions == (42, 102, 1277, 822))


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