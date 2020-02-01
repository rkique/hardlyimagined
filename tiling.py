# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 15:08:27 2019

@author: EricX21
This allows you to create brightness-adjusted collages that match a target image's profile.
"""
from PIL import Image, ImageStat
import random;
imagesArray = [];
boxArray = [];
leftUpBoundsArray = [];
#width and height of canvas (final) image.
width = 1024
height = 1024

#vertical (wDivs) and horizontal (hDivs) dividers!
wDivs = 8;
hDivs = 8;
wunit = int(width/wDivs);
hunit = int(height/hDivs);

#Specify the image that you want to replicate the brightness profile for
GANimage = Image.open("TargetImage.png") 

#Add all collageable images to imagesArray; below is an example for PNGs titled "Screenshot".
for i in range(180,640):
    try:
        imagesArray.append(Image.open("Screenshot ("+str(i)+").png"))
    except:
        pass;

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

for i in range(0,wDivs):
    for j in range(0,hDivs):
        boxArray.append([wunit*i,hunit*j,wunit*(i+1), hunit*(j+1)]);
        leftUpBoundsArray.append((wunit*i,hunit*j))

#creates the collage and saves it to a canvas image.
canvas = Image.new(mode = "RGBA", size = (width,height))
bP = brightnessProfile(GANimage, boxArray);
for i in range(0,wDivs):
    for j in range(0,hDivs):
        boxArray.append([500+wunit*i,hunit*j,500+wunit*(i+1), hunit*(j+1)]);
        leftUpBoundsArray.append((500+wunit*i,hunit*j))
for i in range(0,wDivs*hDivs):
    while True:
        choice = random.randint(0,len(imagesArray)-1)
        img = imagesArray[choice]
        width, height = img.size   # Get dimensions
        left = (width - 1024)/2
        top = (height - 1024)/2
        right = (width + 1024)/2
        bottom = (height + 1024)/2
        img= img.crop((left, top, right, bottom))
        img = img.crop(boxArray[i]);
        if abs(brightness(img)-bP[i]) < 10:
            break;
    canvas.paste(img, leftUpBoundsArray[i], img);
canvas.show();
#name your canvas image here!
a="BrightnessProfileCollage"
canvas.save(a+'.png');

   
