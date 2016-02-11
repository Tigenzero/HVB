import os
import time
import win32api
import PIL
from PIL import Image, ImageGrab
import logging
from window_finder import scanner
import window_finder
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
                result_sum = self.image.getpixel((temp_point, y))
                if len(result_sum) > 3:
                    result_sum = (result_sum[0], result_sum[1], result_sum[2])
                if result_sum == target:
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
                result_sum = self.image.getpixel((x, temp_point))
                if len(result_sum) > 3:
                    result_sum = (result_sum[0], result_sum[1], result_sum[2])
                if result_sum == target:
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

    @classmethod
    def get_window(cls):
        """
        performs the necessary steps to create a full ScreenGrabber object
        returns: a ScreenGrabber object
        """
        window_grabber = cls()
        window_grabber.refresh_image()
        window = window_finder.scanner.Scanner.run(window_grabber.screen_width,
                                                   window_grabber.screen_height,
                                                   window_grabber.scan_size,
                                                   window_grabber.image,
                                                   WINDOW_COLORS)
        left = window_grabber.find_left(window)
        top = window_grabber.find_top(left, window[1])
        window_grabber.window_dimensions = (left, top, left + 1235, top + 720)
        window_grabber.refresh_image()
        return window_grabber

    @classmethod
    def get_window_test(cls, image):
        """
        performs the necessary steps to create a full ScreenGrabber object
        image: unedited screen capture of the window
        returns: a ScreenGrabber object
        """
        window_grabber = cls()
        window_grabber.image = image
        window = window_finder.scanner.Scanner.run(window_grabber.screen_width,
                                                   window_grabber.screen_height,
                                                   window_grabber.scan_size,
                                                   window_grabber.image,
                                                   WINDOW_COLORS)
        left = window_grabber.find_left(window)
        top = window_grabber.find_top(left, window[1])
        window_grabber.window_dimensions = (left, top, left + 1235, top + 720)
        window_grabber.image = window_grabber.image.crop(window_grabber.window_dimensions)
        return window_grabber

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
