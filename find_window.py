import os
import time
import win32api
import scanner
import PIL
from PIL import Image, ImageGrab
import logging
"""
 The initial test will involve 1920X1080
 The width of the box will be at least 1293px
"""
WINDOW_COLORS = [
    (237, 235, 223),
    (227, 224, 209),
    (177, 185, 194)
]


class ScreenGrabber(object):
    def __init__(self):
        self.screen_width = win32api.GetSystemMetrics(0)
        self.screen_height = win32api.GetSystemMetrics(1)
        self.window_dimensions = [0, 0, self.screen_width, self.screen_height]
        self.scan_size = 12
        self.image = None

    def find_left(self, window):
        x = window[0]
        y = window[1]
        count = 0
        last_x = 0
        for i in range(1, x):
            if count >= 150:
                return last_x
            temp_point = x - i
            for target in WINDOW_COLORS:
                if self.image.getpixel((temp_point, y)) == target:
                    last_x = temp_point
                    count = 0
                else:
                    count += 1
        return last_x

    def find_top(self, x, y):
        count = 0
        last_y = 0
        for i in range(1, y):
            if count >= 150:
                return last_y
            temp_point = y - i
            for target in WINDOW_COLORS:
                if self.image.getpixel((x, temp_point)) == target:
                    last_y = temp_point
                    count = 0
                else:
                    count += 1

        return last_y

    def refresh_image(self):
        self.image = ImageGrab.grab(self.window_dimensions)

    def save(self):
        self.image.save(os.getcwd() + '\\image_snap__' + str(int(time.time())) + '.png', 'PNG')

    def save_all(self):
        full_image = ImageGrab.grab()
        full_image.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

"""#for fullscreen
def find_browser():
    im = window_screenGrab()
    temp_point = -1
    #while temp_point != orig_point:
    for i in range(1, 100):
        temp_point = 100 - i
        if im.getpixel((0, temp_point)) != (237, 235, 223) and im.getpixel((0, temp_point)) != (227, 224, 209):
            return temp_point + 1
    print "no point was found, must have been 0"
    return 0"""
