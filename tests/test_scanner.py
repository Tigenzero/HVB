from PIL import Image
import PIL
import win32api
import logging
import scanner
import os


TEST_IMAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_full_window.png")
WINDOW_COLORS = [
    (237, 235, 223),
    (227, 224, 209),
    (177, 185, 194)
]
SCREEN_WIDTH = win32api.GetSystemMetrics(0)
SCREEN_HEIGHT = win32api.GetSystemMetrics(1)
SCAN_SIZE = 12
IMAGE = Image.open(TEST_IMAGE)
IMAGE.convert('RGB')


def test_scanner_init():
    scan_module = scanner.Scanner(SCREEN_WIDTH, SCREEN_HEIGHT, SCAN_SIZE, IMAGE, WINDOW_COLORS)


def test_scanner_scan():
    scan_module = scanner.Scanner(SCREEN_WIDTH, SCREEN_HEIGHT, SCAN_SIZE, IMAGE, WINDOW_COLORS)
    assert(scan_module._scan() is True)


def test_scanner_run():
    corner = scanner.Scanner.run(SCREEN_WIDTH, SCREEN_HEIGHT, SCAN_SIZE, IMAGE, WINDOW_COLORS)
    logging.info(corner)
    assert(corner == (120, 225))