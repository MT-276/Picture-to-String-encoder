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


Image_path = r"E:\Python Programs\Github\Picture-to-String-encoder\Test_picture.png"
option = "D"

from PIL import Image
import os,sys,time

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

im = Image.open(Image_path)
pix = im.load()

m,n=im.size

if option == "E":
    Encoded =""
    for i in range(m):
        for j in range(n):
            tup = pix[j,i]
            for k in tup:
                E,C = Encode(k)
                Encoded+=str(E)
                Encoded+=str(C)
    print(Encoded)

if option == "D":
    Decoded_lst1 = []
    Decoded_lst = []
    Encoded_str = ''
    Encoded_lst = []
    Encoded_inp = "9jYx7Rx=5^=x2ORR0K==7jc#7h==7~M#0c^^9jxY9~YY9@%e4exx2#Yx9@%e8Kd$"
    c=1
    for o in Encoded_inp:
        Encoded_str+=o
        if c % 4 == 0:
            Encoded_lst.append(Encoded_str)
            Encoded_str=''

        c+=1

    for o in Encoded_lst:
        Decoded_lst.append(Decode(o))

    c=1
    for o in Decoded_lst:
        Decoded_lst1.append(o)
        if c % 4 == 0:
            R = Decoded_lst1[0]
            G = Decoded_lst1[1]
            B = Decoded_lst1[2]
            A = Decoded_lst1[3]


        c+=1


'''
im.save('Computed_picture.png')
os.startfile('Computed_picture.png')
'''