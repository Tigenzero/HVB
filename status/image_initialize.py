import os.path
from ntpath import split, basename
import logging

from PIL import Image
from numpy import array, sort
from ImageOps import grayscale


def list_files(file_type):
    r = []
    path = os.getcwd() + "\\images\\initialize\\" + file_type
    logging.debug("Pulling Images from: {}".format(path))
    subdirs = [x[0] for x in os.walk(path)]
    for subdir in subdirs:
        files = os.walk(subdir).next()[2]
        if (len(files) > 0):
            for file in files:
                r.append(subdir + "/" + file)
    return r


def return_filename(path):
    head, tail = split(path)
    return tail or basename(head)


def print_collection(collection):
    logging.debug("Collection length: {}".format(len(collection)))
    for key, value in sort(collection.items()):
        logging.debug("{}: {}".format(value, key))


def get_status_images():
    collection = {}
    for image in list_files("status"):
        im = Image.open(image, 'r')
        im = grayscale(im)
        a = array(im.getcolors())
        a = a.sum()
        filename = return_filename(image).split(".")[0]
        collection[a] = filename
    return collection


def get_skill_images():
    active_collection = {}
    for image in list_files("active"):
        im = Image.open(image, 'r')
        pix_val = list(im.getdata())
        pix_val_flat = [x for sets in pix_val for x in sets]
        a = sum(pix_val_flat)
        filename = return_filename(image).split(".")[0]
        active_collection[a] = filename
    inactive_collection = {}
    for image in list_files("inactive"):
        im = Image.open(image, 'r')
        pix_val = list(im.getdata())
        pix_val_flat = [x for sets in pix_val for x in sets]
        a = sum(pix_val_flat)
        filename = return_filename(image).split(".")[0]
        inactive_collection[a] = filename
    return active_collection, inactive_collection