from PIL import Image
import os
import re
__author__ = 'dusti'

cwd_dir_files = os.listdir(os.getcwd())

for file in cwd_dir_files:
    if re.search("\.png$", file):
        name = file.split('.')
        im = Image.open(file)
        box = (875, 1650, 2675, 1750)
        crop = im.crop(box)
        crop.save(name[0] + '_CROP.png')