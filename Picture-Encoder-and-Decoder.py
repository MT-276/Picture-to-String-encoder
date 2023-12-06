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

print("Image Encoder and Decoder\nDeveloped by  : <MS Productions>\nCopyright     : (c)MS Productions\n")
option = input("Encode Image [E] or Decode string [D] :")

Debug_mode = True

Loaded = False
c=0
while Loaded != True:
    try:
        from PIL import Image                                       #Importing third-party libraries
        import os,sys,time,random
        Loaded = True
    except:
        print("\n[ERROR] An error occured while loading libraries\nAttempting to download libraries...")
        from os import system
        system("pip install Pillow --user")                         #Attempting to download libraries if not found
    if c == 2:
        print("[ERROR] An error occured while loading libraries. Please Re-run the program")
        sys.exit()
    c+=1


#---------------------- Fuctions ----------------------

def Encode(Nums):
    Nums = str(Nums)

    if len(Nums) != 3:                                              # Checks if the provided data is a 3 digit no. or not
        p = 3-len(Nums)
        for v in range(p):
            Nums+="N"                                               # If not then it adds 'N' which just signifies "none"

    Computed_nums_lst = []
    Computed_nums = ""

    #      0   1   2   3   4   5   6   7   8   9   N
    l1 = ["a","b","c","d","e","f","g","h","i","j","x"]              # Key,Value table
    l2 = ["K","L","M","N","O","P","Q","R","S","T","Y"]
    l3 = ["!","@","#","$","%","^","&","*","-","~","="]

    Key = random.randint(0,9)                                       # Selects a random Key

    for i in Nums:
        if i != "N":
            pointer = int(i)+Key                                    # Adds the key to the numeric value of the colour
            if pointer >= 10:
                pointer = pointer - 10                              # If it is greater than 10, it loops around.

            Hash = random.randint(1,3)                              # Selecting one of the char lists

            if Hash == 1:
                Computed_nums_lst.append(l1[pointer])
            if Hash == 2:
                Computed_nums_lst.append(l2[pointer])
            if Hash == 3:
                Computed_nums_lst.append(l3[pointer])
        else:                                                       # Else condition where value of 'i' is "none"
            Hash = random.randint(1,3)
            if Hash == 1:
                Computed_nums_lst.append(l1[10])
            if Hash == 2:
                Computed_nums_lst.append(l2[10])
            if Hash == 3:
                Computed_nums_lst.append(l3[10])

    for j in Computed_nums_lst:
        Computed_nums += j



    return Key,Computed_nums                                        # Returns Key and Encoded colour data

def Decode(Hashed_str):

    decoded = ""

    #      0   1   2   3   4   5   6   7   8   9   N
    l1 = ["a","b","c","d","e","f","g","h","i","j","x"]              # Key-Value table
    l2 = ["K","L","M","N","O","P","Q","R","S","T","Y"]
    l3 = ["!","@","#","$","%","^","&","*","-","~","="]

    Key = int(Hashed_str[0])                                        # Obtains the Key
    Value = Hashed_str[1:4]                                         # Obtains the Value

    for i in Value:                                                 # Checks index of the number in value
        if i in l1:
            pointer = l1.index(i)
        if i in l2:
            pointer = l2.index(i)
        if i in l3:
            pointer = l3.index(i)

        pointer -= Key                                              # Subtracts using key to get real number

        if pointer<0:
            pointer+=10

        if i != "x" and i != "Y" and i != "=":                      # Checks for 'x','Y','=' which signify "none"
            decoded+=str(pointer)

    del Key,Value,pointer,l1,l2,l3                                  # Deleting un-used variables to save RAM

    return decoded                                                  # Returns decoded colour value

def Convert_to_JPG(path):
    F = path.split('\\')
    F = F[-1]
    F = F.split(".")
    F = F[0]
    new_path = F+".jpg"
    im = Image.open(path)
    im4 = im.convert('RGB')                                         # Converting to jpg format
    im4.save(new_path)                                              # Saving temp jpg image

    del im4                                                         # Deleting un-used variables to save RAM
    return new_path


    #---------------------- Main ----------------------


if option == "E":

    #---------------------- Loading Image ----------------------
    Loaded = False
    c = 0
    while Loaded != True:
        print()
        Image_path = input("Enter path of the image : ")            # User input for path of Img.

        if '"' in Image_path:
            Image_path = Image_path.replace('"','')
        try:

            F = path.split('\\')
            F = F[-1]
            F = F.split(".")
            F = F[1]
            Delete = False
            if F != "jpg":
                Image_path = Convert_to_JPG(Image_path)             # This program works only on jpg files and hence
                Delete = True                                       # will convert any non-jpg files to a temp jpg
            im = Image.open(Image_path)                             # and will delete the temp jpg after execution
            start_time = time.perf_counter ()
            Loaded = True
        except Exception as e:
            print(f"[ERROR] {e}")
            if Debug_mode == True:
                print("\n",Image_path)
        if c == 5:
            print("The path of the image is invalid")
            sys.exit()
        c+=1

    pix = im.load()                                                 # Loading the image
    m,n=im.size                                                     # Obtaining size of image
    Encoded =""

    del Loaded,F
    #---------------------- Encoding ----------------------         # Start of Encoding process

    print("\nEncoding image...")


    try:
        F = path.split('\\')
        F = F[-1]
        F = F.split(".")
        F = F[0]
        F = "Encoded_"+F+".txt"                                     # Creates the file where the encoding is going
        file = open(F, 'w')                                         # to be stored while encoding.
    except:
        print("[ERROR] Could not save encoding. Check Disk space")
        sys.exit()



    for i in range(m):                                          # m = no. of rows
        for j in range(n):                                      # n = no. of columns
            tup = pix[i,j]                                      # pix[i,j] --> Gets the RGB data of the pixel
            for k in tup:
                E,C = Encode(k)                                 # RGB value encoded via Encode() function
                Encoded+=str(E)
                Encoded+=str(C)
                file.write(Encoded)                             # [NEW] Directly saving to txt file instead of RAM.
                Encoded = ''

    file.write("."+str(m)+"?"+str(n))
    file.close()

    del m,n,i,j,tup,k,E,C
    print("Image Encoded")

    if Delete == True:                                              # Checks if there was a temp JPG image created
          os.remove(Image_path)                                     # in case the image was of a different format
    del Delete,F,Encoded,file                                       # and deletes it.


if option == "D":

    #---------------------- Decode Loading ----------------------
    Decoded_lst = []
    Decoded_lst1 = []
    pixel_data = []
    Encoded_str = ''

    Loaded = False
    c=0
    while Loaded != True:
        try:
            Encoded_file_name = input("Enter Encoded file path : ") # User input for path of encoded file path

            F = path.split('\\')
            F = F[-1]
            F = F.split(".")
            F = F[-1]
            if F != "txt":                                          # Checks if the file format is correct or not
                print("[ERROR] File format incorrect")
                sys.exit()

            with open(Encoded_file_name, 'r') as file:
                Encoded_inp = file.read()                           # Loades file contents in a variable [Encoded_inp]
            Loaded = True
            start_time = time.perf_counter ()                       # Starts recording time for execution

        except Exception as e:
            print(f"[ERROR] {e}")
            if Debug_mode == True:
                print(Encoded_file_name)
        if c == 5:
            print("The path of the image is invalid")
            sys.exit()
        c+=1

    del F,c,Loaded                                                  # Deleting un-used variables to save RAM

    #---------------------- Decoding ----------------------
    print("\nDecoding...")

    c=1
    try:
        pixel_encoding = Encoded_inp.split(".")
        # The encoding has two parts:
        #       (1) The pixel's encoding
        #       (2) The image's dimensions
        # The pixel's encoding and The image's dimensions
        # are separted by a "."


        for Char in pixel_encoding[0]:                              # Seperates chunks of encoded pixel data
            Encoded_str+=Char
            if c % 4 == 0:
                Decoded_lst.append(Decode(Encoded_str))             # Decodes encoded pixel data
                Encoded_str=''
            c+=1


        c=1

        for Char in Decoded_lst:
            Decoded_lst1.append(Char)
            if c % 3 == 0:
                R = int(Decoded_lst1[0])
                G = int(Decoded_lst1[1])
                B = int(Decoded_lst1[2])
                #A = int(Decoded_lst1[3])
                #print("(",R,",",G,",",B,",",A,")")
                pixel_data.append((R,G,B))                          # Joins all the un-organised pixel data
                Decoded_lst1 = []
            c+=1

        del Decoded_lst,Encoded_str                                 # Deleting un-used variables to save RAM

        Dimension_lst = Encoded_inp.split(".")[1]
        Dimension_lst = Dimension_lst.split("?")
        m,n = int(Dimension_lst[0]),int(Dimension_lst[1])           # Gets dimension data from Encoded_inp
    except:
        print("\n[ERROR] Decryption Failed. Please verify file contents")
        sys.exit()

    del Encoded_inp                                                 # Deleting un-used variables to save RAM

    #---------------------- Converting into an image ----------------------
    x,y=0,0
    print("File Decoded\n\nInitializing image generation...")

    try:
        image = Image.new('RGB', (m, n))                            # Creates a new image

        index = -1
        for x in range(m):
            for y in range(n):
                index += 1

                color = pixel_data[index]
                image.putpixel((x, y), color)                       # Assigns colour to pixel using xy co-ordinate data
        print("Image Generated succesfully")
    except:
        print("\n[ERROR] Image Generation Failed")
        if Debug_mode == True:
            print("\n",m,"x",n,"\n",index,"\n",Encoded_file_name)
        sys.exit()


    #---------------------- Saving Image ----------------------
    print("\nSaving Image...")

    try:
        image.save('Decoded_picture.jpg')                           # Saves the generated image in the same dir, where the program is being executed
    except:
        print("[ERROR] Image was not saved. Check Disk space")
        sys.exit()
    print("Image saved succesfully")
    os.startfile('Decoded_picture.jpg')                             # Opens the saved image

if option != 'E' and option != 'D':
    print("\n[ERROR] Please specify using 'E' and 'D' only")

if Debug_mode == True:
    end_time = time.perf_counter ()
    ao = (end_time - start_time)//1
    if ao>=60:
        ao = str(ao//60) +" Min " + str(ao%60)
    print("\nTime for execution : ",int(ao), "Sec")                 # Calculates and prints the time taken for execution of the program