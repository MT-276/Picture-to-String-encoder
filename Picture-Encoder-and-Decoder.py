#-------------------------------------------------------------------------------
# Name:        Picture-Encoder-and-Decoder
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
print("Image Encoder and Decoder\nDeveloped by  : <MS Productions>\nCopyright     : (c)MS Productions\n")
option = input("Encode Image [E] or Decode string [D] :")

Debug_mode = True

Loaded = False
while Loaded != True:
    try:
        from PIL import Image
        import os,sys,time
        Loaded = True
    except:
        print("\n[ERROR] An error occured while loading libraries\nAttempting to download libraries...")
        from os import system
        system("pip install Pillow")


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

def Convert_to_PNG(path):
    F = "muk\muk"
    F = F.replace("muk","")
    F = path.split(F)
    F = F[-1]
    F = F.split(".")
    F = F[0]
    new_path = F+".png"
    im = Image.open(path)
    im4 = im.convert('RGBA')
    im4.save(new_path)

    del im4
    return new_path

#---------------------- Main ----------------------


if option == "E":
    start_time = time.time()
    #---------------------- Loading Image ----------------------
    Loaded = False
    while Loaded != True:
        print()
        Image_path = input("Enter path of the image : ")
        Image_path = Image_path.replace('"',"")
        try:

            F = "muk\muk"
            F = F.replace("muk","")
            F = Image_path.split(F)
            F = F[-1]
            F = F.split(".")
            F = F[1]
            Delete = False
            if F != "png":
                Image_path = Convert_to_PNG(Image_path)
                Delete = True
            im = Image.open(Image_path)
            Loaded = True
        except:
            print("The path of the image is invalid, please try again!")
            if Debug_mode == True:
                print("\n",Image_path)

    pix = im.load()
    m,n=im.size
    Encoded =""

    del Loaded,F
    #---------------------- Encoding ----------------------
    print("\nEncoding image...")

    for i in range(m):
        for j in range(n):
            tup = pix[i,j]
            for k in tup:
                E,C = Encode(k)
                Encoded+=str(E)
                Encoded+=str(C)
    Encoded+="."+str(m)+"?"+str(n)

    del m,n,i,j,tup,k,E,C
    print("Image Encoded")
    #---------------------- Saving Encryption ----------------------

    print("\nSaving Image Encoding...")
    F = "muk\muk"
    F = F.replace("muk","")
    F = Image_path.split(F)
    F = F[-1]
    F = F.split(".")
    F = F[0]
    F = "Encoded_"+F+".txt"
    file = open(F, 'w')
    file.write(Encoded)
    file.close()

    print("Encoding saved successfully")

    if Delete == True:
          os.remove(Image_path)
    del Delete,F,Encoded,file
    if Debug_mode == True:
        print("Time for execution : %s seconds" % (time.time() - start_time))

    sys.exit()


if option == "D":
    start_time = time.time()
    #---------------------- Decode Loading ----------------------
    Decoded_lst = []
    Decoded_lst1 = []
    pixel_data = []
    Encoded_str = ''
    Encoded_lst = []
    c=1

    Loaded = False
    while Loaded != True:
        try:
            Encoded_file_name = input("Enter Encoded file path : ")
            with open(Encoded_file_name, 'r') as file:
                Encoded_inp = file.read()
            Loaded = True
        except:
            print("[ERROR] File path incorrect. Please try again")
            if Debug_mode == True:
                print(Encoded_file_name)


    #---------------------- Decoding ----------------------
    print("\nDecoding...")
    try:
        e = Encoded_inp.split(".")
        for o in e[0]:
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
        Dimension_lst = Encoded_inp.split(".")[1]
        Dimension_lst = Dimension_lst.split("?")
        m,n = int(Dimension_lst[0]),int(Dimension_lst[1])
        c=0
        print("File Decoded\n\nInitializing image generation...")
    except:
        print("\n[ERROR] Decryption Failed. Please verify file contents")
        sys.exit()
    #---------------------- Converting into an image ----------------------
    try:
        image = Image.new('RGBA', (m, n))
        #print(m,"x",n)
        #print(len(pixel_data))

        index = -1
        for x in range(m):
            for y in range(n):
                index += 1

                color = pixel_data[index]
                image.putpixel((x, y), color)
        print("Image Generated succesfully")
    except:
        print("\n[ERROR] Image Generation Failed")
        if Debug_mode == True:
            print("\n",m,"x",n,"\n",index,"\n",Encoded_file_name)

        sys.exit()
    #---------------------- Saving Image ----------------------
    print("\nSaving Image...")
    try:
        image.save('Decoded_picture.png')
    except:
        print("\n[ERROR] Image saving failed")
        sys.exit()
    print("Image saved succesfully")
    os.startfile('Decoded_picture.png')
    if Debug_mode == True:
        print("Time for execution : %s seconds" % (time.time() - start_time))
    sys.exit()

if option != 'E' and option != 'D':
    print("\n[ERROR] Please specify using 'E' and 'D' only")
    sys.exit()