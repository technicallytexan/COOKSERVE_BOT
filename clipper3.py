from PIL import Image
import os
import re
__author__ = 'dusti'

cwd_dir_files = os.listdir(os.getcwd())
file = cwd_dir_files[0]
# file = 'LARGE DIET.png'
name = file.split('.')
im = Image.open(file)
# 4TH SLOT
box = (257, 256, 640, 385)
crop = im.crop(box)
crop.save(name[0] + '_PSCROP.png')


'''from PIL import Image
import os
import re
__author__ = 'dusti'

cwd_dir_files = os.listdir(os.getcwd())
file = cwd_dir_files[0]
# file = 'THE YELLOW DOG.png'
if re.search("\.png$", file):
    name = file.split('.')
    im = Image.open(file)
    # 1ST SLOT
    # box = (257, 256, 640, 385)
    # 4TH SLOT
    box = (257, 773, 640, 901)
    crop = im.crop(box)
    crop.save(name[0] + '_PSCROP.png')'''