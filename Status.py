import ImageOps
import ImageGrab
from numpy import *
from Coordinates import Cord
from Settings import *
import time
import os

class Status:
    channeling = 10527
    protection = 9619
    shadow_veil = 7476
    hastened = 10229
    nothing = 1162
    spirit_shield = 7827
    heartseeker = 6340
    special_2 = 2620
    special_1 = 1860
    health_pot = 8461
    mana_pot = 6516
    spirit_pot = 0
    regen = 7292
    collection = {channeling: 'channeling',
                  protection: 'protection',
                  shadow_veil: 'shadow_veil',
                  hastened: 'hastened',
                  spirit_shield: 'spirit_shield',
                  heartseeker: 'heartseeker',
                  special_1: 'special_1',
                  special_2: 'special_2',
                  health_pot: 'health_pot',
                  mana_pot: 'mana_pot',
                  spirit_pot: 'spirit_pot',
                  regen: 'regen'}


def lookup_status(pixel_sum):
    for known_status in Status.collection:
        if pixel_sum == known_status:
            #print "status found: %s" % Status.collection.get(known_status)
            return Status.collection.get(known_status)
    return " "


def get_status():
    Cord.Current_Status = []
    for status in Cord.Status:
        pixel_sum = get_pixel_sum(status)
        if pixel_sum == Status.nothing:
            return
        lookup = lookup_status(pixel_sum)
        if len(lookup) > 1:
            Cord.Current_Status.append(lookup)


def get_pixel_sum(box):
    im = ImageOps.grayscale(ImageGrab.grab((Settings.box[0] + box[0], Settings.box[1] + box[1], Settings.box[0] + box[2], Settings.box[1] + box[3])))
    a = array(im.getcolors())
    a = a.sum()
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_pixel_sum_color(box, save):
    im = ImageGrab.grab((Settings.box[0] + box[0], Settings.box[1] + box[1], Settings.box[0] + box[2], Settings.box[1] + box[3]))
    a = array(im)
    a = a.sum()
    if save:
        im.save(os.getcwd() + '\\unknown_item__x-' + str(box[0]) + '_y-' + str(box[1]) + '_' + str(int(time.time())) + '.png', 'PNG')
    return a


def is_status_active(status_name):
    for status in Cord.Current_Status:
        if status == status_name:
            return True
    return False
