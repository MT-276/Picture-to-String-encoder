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
'''Information from the Dev:
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

def Encode(Nums):

    import random,os,sys,time
    Computed_nums_lst = []
    Computed_nums = ""

    #      0   1   2   3   4   5   6   7   8   9
    l1 = ["a","b","c","d","e","f","g","h","i","j"]
    l2 = ["K","L","M","N","O","P","Q","R","S","T"]
    l3 = ["!","@","#","$","%","^","&","*","-","~"]

    Encoder_value = random.randint(0,9)

    for i in str(Nums):
        pointer = int(i)+Encoder_value
        if pointer >= 10:
            pointer = pointer - 10

        Hash = random.randint(1,3)

        if Hash == 1:
            Computed_nums_lst.append(l1[pointer])
        if Hash == 2:
            Computed_nums_lst.append(l2[pointer])
        if Hash == 3:
            Computed_nums_lst.append(l3[pointer])
    for j in Computed_nums_lst:
        Computed_nums += j

    return Encoder_value,Computed_nums

def Decode(Hashed_str):

    decoded = ""

    #      0   1   2   3   4   5   6   7   8   9
    l1 = ["a","b","c","d","e","f","g","h","i","j"]
    l2 = ["K","L","M","N","O","P","Q","R","S","T"]
    l3 = ["!","@","#","$","%","^","&","*","-","~"]

    Key = int(Hashed_str[0])
    Value = Hashed_str[1:4]

    for i in Value:
        if i in l1:
            pointer = l1.index(i)
        if i in l2:
            pointer = l2.index(i)
        if i in l3:
            pointer = l3.index(i)

        pointer -= Key
        if pointer<0:
            pointer+=10
        decoded+=str(pointer)

    print(decoded)

# Image path : r"E:\Python Programs\Github\Picture-to-String-encoder\Test_picture.png"

x,y = 4,5

im = Image.open('Test_picture.png')
pix = im.load()
print (im.size)
print (pix[x,y])
pix[x,y] = (255,0,0,255)               # Set the RGBA Value of the image (tuple)
im.save('Computed_picture.png')
os.startfile('Computed_picture.png')
