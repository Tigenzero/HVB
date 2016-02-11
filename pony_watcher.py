import time
import logging
import winsound
import random

from window_finder.find_window import ScreenGrabber
from click_press import press


class PonyWatcher(object):
    def __init__(self):
        # (518,  185) TEST
        self.pony_check_loc = ((706, 170), (760, 122))
        self.pony_check_color = (237, 235, 223)

    def is_pony_time(self, image, pony_loc=(0, 0)):
        if pony_loc == (0, 0):
            pony_loc = self.pony_check_loc[0]
        if image.getpixel(pony_loc) != self.pony_check_color:
            return True
        else:
            return False

    def pony_time_safety_check(self, screen_grabber):
        if type(screen_grabber) is not ScreenGrabber:
            raise ValueError("During activation of Pony Time, object screen_grabber was not of type ScreenGrabber.")
        if not self.is_pony_time(screen_grabber.image):
            return
        time.sleep(0.5)
        screen_grabber.refresh_image()
        for pony_loc in self.pony_check_loc:
            if self.is_pony_time(screen_grabber.image, pony_loc):
                continue
            else:
                return
        logging.info("Pony Time Activated")
        self.activate_pony_time(screen_grabber)
        return

    def activate_pony_time(self, screen_grabber=ScreenGrabber()):
        """
        Activates the Pony Time protocol.
        The user is alerted with a sound and the activation lasts for 20 seconds.
        If no user response is had, the activation inputs a random letter and presses enter.
        :param screen_grabber: ScreenGrabber object
        :return: None
        """
        pony_timer = 0
        while self.is_pony_time(screen_grabber.image):
            self._play_pony_sound()
            time.sleep(4)
            pony_timer += 1
            screen_grabber.refresh_image()
            if pony_timer >= 5:
                self._activate_pony_time_emergency_response()
                return

    def _activate_pony_time_emergency_response(self):
        press('backspace')
        time.sleep(0.2)
        option = random.randint(0, 2)
        if option == 0:
            press('a')
        if option == 1:
            press('b')
        if option == 2:
            press('c')
        press('enter')
        pass

    def _play_pony_sound(self):
        freq = 2500  # Set Frequency To 2500 Hertz
        dur = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(freq, dur)
        return
