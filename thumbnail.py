# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 15:39:01 2019

@author: EricX21

This file creates a (centered) 256x256 PNG thumbnail of all other files in the current directory. 
Useful for formatting purposes.
"""

from PIL import Image
import glob, os
size = 256,256
new_width = 1080
new_height = 1080
i = 0

for infile in glob.glob("*"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    width, height = im.size   # Get dimensions

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    im = im.crop((left, top, right, bottom))
    im.thumbnail(size)
    im.save("Image "+str(i)+".png","PNG");
    i= i+1;