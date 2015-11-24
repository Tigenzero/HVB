from coordinates import StatusCords
from numpy import *
import image_initialize


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
    def __init__(self):
        self.current_status = []
        self.status_coordinates = StatusCords()
        self.status_types = StatusType()
        self.status_collection = image_initialize.get_status_images()

    def refresh_status(self, image):
        for status in self.status_coordinates.status_locs:
            pixel_sum = array(image.crop(status).getcolors()).sum()
            if pixel_sum == self.status_types.nothing:
                return
            lookup = self.lookup_status(pixel_sum)
            if len(lookup) > 1:
                self.current_status.append(lookup)

    def lookup_status(self, pixel_sum):
        for known_status in self.status_collection:
            if pixel_sum == known_status:
                #print "status found: %s" % Status.collection.get(known_status)
                return self.status_collection.get(known_status)
        #logging.debug("status not found: {0}".format(pixel_sum))
        return " "