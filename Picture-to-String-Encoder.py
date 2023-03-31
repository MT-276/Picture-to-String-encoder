#-------------------------------------------------------------------------------
# Name:        Picture-to-String-Encoder
# Purpose:
#
# Author:      MS Productions
#
# Created:     31 03 2023
# Copyright:   (c)MS Productions
#
# Lead Dev : Meit Sant (XII)
#-------------------------------------------------------------------------------
'''
Information from the Dev:
    Every pixel has 4 values, i.e RGBA.
    R = Red (255)
    G = Green (255)
    B = Blue (255)
    A = Alpha [Basically the brightness of the colour] (255)
Bibliography :
    (i) https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
'''

from PIL import Image
import os,sys,time

# Image path : r"E:\Python Programs\Github\Picture-to-String-encoder\Test_picture.png"

x,y = 4,5

im = Image.open('Test_picture.png')
pix = im.load()
print (im.size)
print (pix[x,y])
pix[x,y] = (255,0,0,255)               # Set the RGBA Value of the image (tuple)
im.save('Computed_picture.png')
os.startfile('Computed_picture.png')
