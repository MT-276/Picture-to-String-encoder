#-------------------------------------------------------------------------------
# Name:        Picture-to-String-Encoder
# Purpose:
#
# Author:      MS Productions
#
# Created:     31 03 2023
# Copyright:   (c)MS Productions
#
# Lead Dev : Meit Sant
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

option = "D" #input("Encrypt Image [E] or Decrypt Hash [D] :")

from PIL import Image
import os,sys,time


#---------------------- Fuctions ----------------------

def Encode(Nums):
    Nums = str(Nums)
    if len(Nums) != 3:
        p = 3-len(Nums)
        for v in range(p):
            Nums+="N"

    import random,os,sys,time
    Computed_nums_lst = []
    Computed_nums = ""

    #      0   1   2   3   4   5   6   7   8   9   N
    l1 = ["a","b","c","d","e","f","g","h","i","j","x"]
    l2 = ["K","L","M","N","O","P","Q","R","S","T","Y"]
    l3 = ["!","@","#","$","%","^","&","*","-","~","="]

    Encoder_value = random.randint(0,9)

    for i in Nums:
        if i != "N":
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
        else:
            Hash = random.randint(1,3)
            if Hash == 1:
                Computed_nums_lst.append(l1[10])
            if Hash == 2:
                Computed_nums_lst.append(l2[10])
            if Hash == 3:
                Computed_nums_lst.append(l3[10])

    for j in Computed_nums_lst:
        Computed_nums += j

    return Encoder_value,Computed_nums

def Decode(Hashed_str):

    decoded = ""

    #      0   1   2   3   4   5   6   7   8   9   N
    l1 = ["a","b","c","d","e","f","g","h","i","j","x"]
    l2 = ["K","L","M","N","O","P","Q","R","S","T","Y"]
    l3 = ["!","@","#","$","%","^","&","*","-","~","="]

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

        if i != "x" and i != "Y" and i != "=":
            decoded+=str(pointer)

    return decoded

#---------------------- ----------------------


if option == "E":
    #---------------------- Loading Image ----------------------
    Image_path = r"E:\Python Programs\Github\Picture-to-String-encoder\Test_picture.png"
    im = Image.open(Image_path)
    pix = im.load()
    m,n=im.size
    Encoded =""

    #---------------------- Encrypting ----------------------
    for i in range(m):
        for j in range(n):
            tup = pix[j,i]
            for k in tup:
                E,C = Encode(k)
                Encoded+=str(E)
                Encoded+=str(C)
    Encoded+=str(m)
    Encoded+=str(n)

    print(Encoded)

    #---------------------- Saving Encryption ----------------------


if option == "D":

    #---------------------- Decryption Loading ----------------------
    Decoded_lst = []
    Decoded_lst1 = []
    pixel_data = []
    Encoded_str = ''
    Encoded_lst = []
    Encoded_inp = "7RYx1@=Y6gY=3PiS4%==5h!K2cxY0#Pf1$gg2c=x7hY=0#ff7RYY1b==9bOe4gjj22"
    c=1

    #---------------------- Decrypting ----------------------

    for o in Encoded_inp:
        Encoded_str+=o
        if c % 4 == 0:
            Encoded_lst.append(Encoded_str)
            Encoded_str=''

        c+=1
    for o in Encoded_lst:
        Decoded_lst.append(Decode(o))
    c=1
    x=0
    y=0
    for o in Decoded_lst:
        Decoded_lst1.append(o)
        if c % 4 == 0:
            R = int(Decoded_lst1[0])
            G = int(Decoded_lst1[1])
            B = int(Decoded_lst1[2])
            A = int(Decoded_lst1[3])
            #print("(",R,",",G,",",B,",",A,")")
            pixel_data.append((R,G,B,A))
            Decoded_lst1 = []
        c+=1
    #print(pixel_data)
    m,n = int(Encoded_inp[-2]),int(Encoded_inp[-1])
    c=0
    #---------------------- Converting into an image ----------------------

    image = Image.new(mode='RGBA', size=(m, n))
    image.putdata(pixel_data)

    #---------------------- Saving Image ----------------------
    image.save('Computed_picture.png')
    print("Image Generated succesfully")

os.startfile('Computed_picture.png')
