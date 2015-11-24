from PIL import Image
import ImageOps
from numpy import array
H_LIMIT = 40
CURE_LIMIT = 60
REGEN_LIMIT = 70
M_LIMIT = 50
S_LIMIT = 50


def recover_stats(health, mana, spirit):
    if health <= H_LIMIT:
        return 100
    elif health <= CURE_LIMIT:
        return 101
    elif health <= REGEN_LIMIT:
        return 102
    elif mana <= M_LIMIT:
        return 200
    elif spirit <= S_LIMIT:
        return 300
    else:
        return 99


def get_pixel_sum(image, crop_box):
        image_crop = ImageOps.grayscale(image.crop(crop_box))
        a = array(image_crop.getcolors())
        a = a.sum()
        return a


def get_pixel_sum_color(image, crop_box):
        image_crop = image.crop(crop_box)
        a = array(image_crop.getcolors())
        a = a.sum()
        return a