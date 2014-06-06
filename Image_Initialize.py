from PIL import Image
from numpy import *
import os
import ntpath
from Skills import Skills
import ImageOps
from Status import Status
import Items

def get_images():
    for image in list_files("active"):
        im = Image.open(image, 'r')
        im = ImageOps.grayscale(im)
        a = array(im.getcolors())
        a = a.sum()
        filename = return_filename(image).split(".")[0]
        Skills.Active_Collection[a] = filename
    for image in list_files("inactive"):
        im = Image.open(image, 'r')
        im = ImageOps.grayscale(im)
        a = array(im.getcolors())
        a = a.sum()
        filename = return_filename(image).split(".")[0]
        Skills.Inactive_Collection[a] = filename
    for image in list_files("status"):
        im = Image.open(image, 'r')
        im = ImageOps.grayscale(im)
        a = array(im.getcolors())
        a = a.sum()
        filename = return_filename(image).split(".")[0]
        Status.collection[a] = filename
    for image in list_files("gem"):
        im = Image.open(image, 'r')
        pix_val = list(im.getdata())
        pix_val_flat = [x for sets in pix_val for x in sets]
        a = sum(pix_val_flat)
        filename = return_filename(image).split(".")[0]
        Items.Gem_Collection[a] = filename
    for image in list_files("item"):
        im = Image.open(image, 'r')
        pix_val = list(im.getdata())
        pix_val_flat = [x for sets in pix_val for x in sets]
        a = sum(pix_val_flat)
        filename = return_filename(image).split(".")[0]
        Items.Item_Collection[a] = filename
        #USE ONLY WHEN COLOR IS NEEDED
        #pix_val = list(im.getdata())
        #pix_val_flat = [x for sets in pix_val for x in sets]
        #a = sum(pix_val_flat)



def list_files(type):
    r = []
    path = os.getcwd() + "\\images\\initialize\\" + type
    subdirs = [x[0] for x in os.walk(path)]
    for subdir in subdirs:
        files = os.walk(subdir).next()[2]
        if (len(files) > 0):
            for file in files:
                r.append(subdir + "/" + file)
    return r


def return_filename(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)