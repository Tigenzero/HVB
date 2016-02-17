import logging

from numpy import *
import ImageOps

from status import image_initialize

from user_interface.coordinates import StatusCords


class StatusType(object):
    def __init__(self):
        self.channeling = 10527
        self.protection = 9619
        self.shadow_veil = 7476
        self.haste = 10229
        self.nothing = 1162
        self.spirit_shield = 7827
        self.heartseeker = 6340
        self.special_2 = 2620
        self.special_1 = 1860
        self.health_pot = 8461
        self.mana_pot = 6516
        self.spirit_pot = 0 #NEED
        self.regen = 7292
        self.overwhelming_strikes = 12726
        self.riddle_master = 8331
        self.spark_life = 15675


class StatusMonitor(object):
    """
    Collects status images and monitors current statuses of player
    NEEDS TO STAY ACTIVE
    """
    def __init__(self):
        self.current_status = []
        self.status_coordinates = StatusCords()
        self.status_types = StatusType()
        self.status_collection = image_initialize.get_status_images()

    def _get_status_sum(self, image, status_box):
        return array(ImageOps.grayscale(image.crop(status_box)).getcolors()).sum()

    def _lookup_status(self, pixel_sum):
        for known_status in self.status_collection:
            if pixel_sum == known_status:
                logging.debug("Status known as {}".format(self.status_collection.get(known_status)))
                return self.status_collection.get(known_status)
        logging.debug("Status Not Known")
        return None

    def is_status_active(self, status_name):
        if status_name in self.current_status:
            return True
        else:
            return False

    def refresh_status(self, image):
        self.current_status = []
        count = 1
        for status in self.status_coordinates.status_locs:
            pixel_sum = self._get_status_sum(image, status)
            logging.debug("Status {}: {}".format(count, pixel_sum))
            count += 1
            if self.status_types.nothing - 100 <= pixel_sum <= self.status_types.nothing + 100:
                logging.debug("pixel sum is too low/high, returning")
                return
            lookup = self._lookup_status(pixel_sum)
            if lookup is not None:
                self.current_status.append(lookup)
                logging.debug("{}: {}".format(lookup, pixel_sum))