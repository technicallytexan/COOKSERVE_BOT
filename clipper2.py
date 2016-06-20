from PIL import Image
import os
import re
__author__ = 'dusti'

cwd_dir_files = os.listdir(os.getcwd())
file = cwd_dir_files[0]
if re.search("\.png$", file):
    name = file.split('.')
    im = Image.open(file)
    # 4TH SLOT
    box = (257, 766, 657, 563)
    crop = im.crop(box)
    crop.save(name[0] + '_PSCROP.png')