import win32api
import logging
import os

from PIL import Image

from window_finder import scanner


TEST_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "test_full_window.png")
WINDOW_COLORS = [
    (237, 235, 223),
    (227, 224, 209),
    (177, 185, 194)
]
TEST_DIMENSIONS = [1357, 831]
SCREEN_WIDTH = TEST_DIMENSIONS[0]
SCREEN_HEIGHT = TEST_DIMENSIONS[1]
SCAN_SIZE = 12
IMAGE = Image.open(TEST_IMAGE)
IMAGE.convert('RGB')


def test_scanner_init():
    scan_module = scanner.Scanner(SCREEN_WIDTH, SCREEN_HEIGHT, SCAN_SIZE, IMAGE, WINDOW_COLORS)


def test_scanner_scan():
    scan_module = scanner.Scanner(SCREEN_WIDTH, SCREEN_HEIGHT, SCAN_SIZE, IMAGE, WINDOW_COLORS)
    assert scan_module._scan()


def test_scanner_run():
    corner = scanner.Scanner.run(SCREEN_WIDTH, SCREEN_HEIGHT, SCAN_SIZE, IMAGE, WINDOW_COLORS)
    logging.info(corner)
    assert(corner >= (42, 102))