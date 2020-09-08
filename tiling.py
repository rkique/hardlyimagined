# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:08:27 2019

@author: EricX21
"""
from PIL import Image, ImageStat
import glob;
import random;

#number of horizontal tiles
wDivs = 8;
#number of vertical tiles
hDivs = 8;
#name your output image here
savename = "MyFirstCollage"
#write your pathname pattern here. This example is a relative path specifying all PNGs in the GSVImage subfolder.
globMatcher = "./GSVImages/*.png"
#this is the strictness of the brightness match-- higher values give faster, but less accurate matches.
bScope = 10

def brightness(image):
   im = image.convert('L')
   stat = ImageStat.Stat(im)
   return stat.mean[0]

def brightnessProfile(image, boxArray):
    brightnesses = [];
    for box in boxArray:
        img = image.crop(box);
        brightnesses.append(brightness(img));
    return brightnesses;

#Image Collection
imagesArray = [];        
for infile in glob.glob(globMatcher):
    try:       
        imagesArray.append(Image.open(infile))
    except:
        pass;

#Size
size = imagesArray[0].size
wunit = int(imagesArray[0].width/wDivs);
hunit = int(imagesArray[0].height/hDivs);

#Crop Boxes
boxArray = [];
for i in range(0,wDivs):
    for j in range(0,hDivs):
        boxArray.append([wunit*i,hunit*j,wunit*(i+1), hunit*(j+1)]);

#Canvas
canvas = Image.new(mode = "RGBA", size = size)

#brightnessProfile
bP = brightnessProfile(imagesArray[random.randint(0,len(imagesArray)-1)], boxArray);

#Cropping and Pasting
for i in range(0,wDivs*hDivs):
    while True:
        choice = random.randint(0,len(imagesArray)-1)
        img = imagesArray[choice].crop(boxArray[i]);
        if abs(brightness(img)-bP[i]) < bScope:
            break;
    canvas.paste(img, tuple(boxArray[i][:2]), img);
canvas.save(savename+'.png');

   
