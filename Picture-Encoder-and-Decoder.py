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


# Introduction to the program
print('''
Picture String Encoder and Downloader V2.0.0
Developed by     : Meit Sant [Github:MT_276]
Licence          : Apache License Version 2.0
''')

Debug_mode = True

import ctypes

# Importing third-party libraries

try:
    from PIL import Image                                           # Trying to import PIL
except ModuleNotFoundError:
    print("[ERROR] PIL not found. Installing...\n")
    
    exit_code = os.system("pip install Pillow==9.5.0")
    
    if exit_code != 0:
        print("\n[ERROR] Error Code : ",exit_code)
        print("[ERROR] Could not install PIL. Exiting...")
        sys.exit()
        input()
    else:
        print("\n[INFO] PIL installed successfully.\n")
        from PIL import Image                
                              
import os,sys,time,random,_tkinter
from tkinter.filedialog import askopenfilenames
from functools import cache
                                                                
py_ver = sys.version_info                                           # Checking compatibility with the latest features
if py_ver.minor < 9:
    print(f"\n[ERROR] Outdated Python version ({py_ver.major}.{py_ver.minor}).")
    print("[INFO] V 1.1.0 onwards, this program requires Python 3.9 or higher to run.")
    print("       Please use V1.0.0 for older versions of Python.")
    input()
    sys.exit()


try:
    option = input("Encode Image [E] or Decode string [D] : ").upper()
except KeyboardInterrupt:
    print("\n[ERROR] Keyboard Interrupt. Exiting...")
    input()
    sys.exit()

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

@cache
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
    # Get filename without path and extension
    basename = os.path.basename(path)
    filename_without_ext = os.path.splitext(basename)[0]
    new_path = filename_without_ext + ".jpg"
    im = Image.open(path)
    im4 = im.convert('RGB')                                         # Converting to jpg format
    im4.save(new_path)                                              # Saving temp jpg image

    del im4                                                         # Deleting un-used variables to save RAM
    return new_path

def Upscale_Image(image, factor):
    """
    Advanced image upscaling with sharpening and enhancement
    """
    try:
        from PIL import ImageEnhance, ImageFilter
        
        # Get original dimensions
        original_width, original_height = image.size
        new_width = int(original_width * factor)
        new_height = int(original_height * factor)
        
        print(f"    Upscaling from {original_width}x{original_height} to {new_width}x{new_height}...")
        
        # Step 1: High-quality resize using LANCZOS (best for upscaling)
        upscaled = image.resize((new_width, new_height), Image.LANCZOS)
        
        # Step 2: Apply unsharp mask for sharpening
        # Create a slightly blurred version
        blurred = upscaled.filter(ImageFilter.GaussianBlur(radius=0.8))
        
        # Create unsharp mask by subtracting blurred from original
        from PIL import ImageChops
        mask = ImageChops.subtract(upscaled, blurred)
        
        # Apply the mask back to enhance edges
        sharpened = ImageChops.add(upscaled, mask)
        
        # Step 3: Enhance contrast and color
        # Enhance contrast (makes edges more defined)
        contrast_enhancer = ImageEnhance.Contrast(sharpened)
        enhanced = contrast_enhancer.enhance(1.1)  # 10% contrast boost
        
        # Enhance color saturation (makes colors more vibrant)
        color_enhancer = ImageEnhance.Color(enhanced)
        vibrant = color_enhancer.enhance(1.2)  # 20% saturation boost
        
        # Step 4: Final sharpness enhancement
        sharpness_enhancer = ImageEnhance.Sharpness(vibrant)
        final_image = sharpness_enhancer.enhance(1.3)  # 30% sharpness boost
        
        print("    ✓ Image upscaled with advanced enhancement!")
        return final_image
        
    except ImportError:
        # Fallback to basic resize if advanced features not available
        print("    Using basic upscaling (install PIL for advanced features)...")
        new_width = int(image.size[0] * factor)
        new_height = int(image.size[1] * factor)
        return image.resize((new_width, new_height), Image.LANCZOS)
    except Exception as e:
        print(f"    [WARNING] Upscaling failed: {e}")
        print("    Continuing with original image...")
        return image


    #---------------------- Main ----------------------

def Choose_Files(Type):
    '''
    Get the file path from user by opening an Explorer window
    '''
    if Type == 'Img':                                               # Open a Explorer window to choose a file
        
        filenames = askopenfilenames(title = "Select image", filetypes = [("Image files", ("*.png","*.jpg"))])
        ctypes.windll.user32.ShowWindow('Select file', 5)
        ctypes.windll.user32.SetForegroundWindow('Select file')
    if Type == 'Text':                                              # Open a Explorer window to choose a file
        
        filenames = askopenfilenames(title = "Select text file", filetypes = [("Text files", "*.txt")])
        ctypes.windll.user32.ShowWindow('Select file', 5)
        ctypes.windll.user32.SetForegroundWindow('Select file')
    
    if filenames == '':
        return                                                      # If the user closes the window without choosing a file, then do nothing.

    return filenames


if option == "E":

    #---------------------- Loading Image ----------------------

    for c in range(5):
        print("\nPlease Choose the image/images you want to encode :")
        try:
            
            Image_lst = Choose_Files('Img')                                 # User input for path of Img.

        except _tkinter.TclError:                                           # If window was not opened. Then input manual paths.
            print("[ERROR] Could not open explorer window. If encoding multiple images, please use a comma to seperate the paths.")
            Images_path = input("\nPlease enter the path of the image manually: ")
            if '"' in Images_path:
                Images_path = Images_path.replace('"','')
            Image_lst = Images_path.split(',')

        except Exception as e:
            print(f"\n{e}\n[ERROR] Please try again.")
            continue
        
        if Image_lst in ['',None]:                                          # Checks if the user has cancelled the operation
            print("\n[ERROR] Operation Cancelled. Exiting...")
            input()
            sys.exit()

        break

    
    start_time = time.perf_counter ()                                       # Starting timer to find out the time for execution.
    for Image_path in Image_lst:

        try:
            Delete = False
            if Image_path.split(".")[1] != "jpg":                           # Checks if the image is a jpg file or not
                Image_path = Convert_to_JPG(Image_path)                     # This program works only on jpg files and hence
                Delete = True                                               # will convert any non-jpg files to a temp jpg
            im = Image.open(Image_path)                                     # and will delete the temp jpg after execution

        except Exception as e:
            print(f"[ERROR] {e}")
            if Debug_mode == True:
                print("\n",Image_path)
            sys.exit()

        pix = im.load()                                                     # Loading the image
        m,n=im.size                                                         # Obtaining size of image
        Encoded =""

        #---------------------- Encoding ----------------------             # Start of Encoding process

        try:
            # Get filename without path and extension
            basename = os.path.basename(Image_path)
            filename_without_ext = os.path.splitext(basename)[0]
            
            if not os.path.exists("Encoded"):                               # Create a folder "Encoded"
                os.makedirs("Encoded")
            F = "Encoded/Encoded_"+filename_without_ext+".txt"                                 # Creates the file where the encoding is going
            file = open(F, 'w')                                             # to be stored while encoding.
        except Exception as e:
            print(e)
            input()
            sys.exit()

        print(f"\nEncoding image to {F}...")

        for i in range(m):                                                  # m = no. of rows
            for j in range(n):                                              # n = no. of columns
                tup = pix[i,j]                                              # pix[i,j] --> Gets the RGB data of the pixel
                for k in tup:
                    E,C = Encode(k)                                         # RGB value encoded via Encode() function
                    Encoded+=str(E)
                    Encoded+=str(C)
                    file.write(Encoded)                                     # [NEW] Directly saving to txt file instead of RAM.
                    Encoded = ''

        file.write("."+str(m)+"?"+str(n))
        file.close()

        del m,n,i,j,tup,E,C
        print("Image Encoded")

        if Delete == True:                                                  # Checks if there was a temp JPG image created
            os.remove(Image_path)                                           # in case the image was of a different format
        del Delete,F,Encoded,file                                           # and deletes it.

elif option == "D":

    #---------------------- Decode Loading ----------------------

    for c in range(5):
        print("\nPlease Choose the file(s) you want to decode")
        try:
            
            Encoded_lst = Choose_Files('Text')                              # User input for path of encoded file path
            
        except _tkinter.TclError:
            print("[ERROR] Could not open explorer window. If decoding multiple files, please use a comma to seperate the paths.")
            Encoded_path = input("\nPlease enter the path of the file manually: ")
            if '"' in Encoded_path:
                Encoded_path = Encoded_path.replace('"','')
            Encoded_lst = Encoded_path.split(',')
        except Exception as e:
            print(f"\n{e}\n[ERROR] Please try again.")
            continue

        if Encoded_lst in ['',None]:
            print("\n[ERROR] Operation Cancelled. Exiting...")
            input()
            sys.exit()
        break
    
    
    start_time = time.perf_counter ()                                       # Starts recording time for execution                      
    
    # Initialize upscaling variables
    enable_upscaling = False
    upscale_factor = 1.0
    
    for nume,Encoded_img in enumerate(Encoded_lst):
        
        Decoded_lst = []                                                    # Intitializing variables
        Decoded_lst1 = []
        pixel_data = []
        Encoded_str = ''
        
        print(f"\nDecoding {nume+1}) {os.path.basename(Encoded_img)} ...")     # Prints the name of the file being decoded
       
       #---------------------- Loading Encoded File ----------------------
        try:
            with open(Encoded_img, 'r') as file:
                Encoded_inp = file.read()
                
        except Exception as e:                                              # Loades file contents in a variable [Encoded_inp]
            print(f"\n[ERROR] Could not read file {Encoded_img}. Please try again.\n[ERROR] {e} ")
            input()
            sys.exit()
       
        #---------------------- Upscaling Option ----------------------
        if nume == 0:  # Only ask once for all files
            try:
                upscale_choice = input("\nDo you want to upscale the decoded image(s) for enhanced quality? [Y/N]: ").upper()
                if upscale_choice in ['Y', 'YES']:
                    upscale_factor = input("Enter upscale factor (2-4 recommended, default 2): ").strip()
                    try:
                        upscale_factor = float(upscale_factor) if upscale_factor else 2.0
                        upscale_factor = max(1.0, min(upscale_factor, 8.0))  # Limit between 1-8x
                        enable_upscaling = True
                        print(f"    Upscaling enabled with factor: {upscale_factor}x")
                    except ValueError:
                        upscale_factor = 2.0
                        enable_upscaling = True
                        print("    Using default upscale factor: 2.0x")
                else:
                    enable_upscaling = False
                    upscale_factor = 1.0
            except KeyboardInterrupt:
                print("\n[ERROR] Keyboard Interrupt. Exiting...")
                input()
                sys.exit()
        
        #---------------------- Decoding ----------------------

        c=1
        try:
            pixel_encoding = Encoded_inp.split(".")
            # The encoding has two parts:
            #       (1) The pixel's encoding
            #       (2) The image's dimensions
            # The pixel's encoding and The image's dimensions
            # are separted by a "."


            for Char in pixel_encoding[0]:                                  # Seperates chunks of encoded pixel data
                Encoded_str+=Char
                if c % 4 == 0:
                    Decoded_lst.append(Decode(Encoded_str))                 # Decodes encoded pixel data
                    Encoded_str=''
                c+=1
            c=1

            for Char in Decoded_lst:
                Decoded_lst1.append(Char)
                if c % 3 == 0:
                    R = int(Decoded_lst1[0])
                    G = int(Decoded_lst1[1])
                    B = int(Decoded_lst1[2])
                    pixel_data.append((R,G,B))                              # Joins all the un-organised pixel data
                    Decoded_lst1 = []
                c+=1

            Dimension_lst = Encoded_inp.split(".")[1]
            Dimension_lst = Dimension_lst.split("?")
            m,n = int(Dimension_lst[0]),int(Dimension_lst[1])               # Gets dimension data from Encoded_inp
        except Exception as e:
            print("\n[ERROR] Decryption Failed. Please verify file contents")
            print(f"[ERROR] {e}")
            input()
            sys.exit()


        #---------------------- Converting into an image ----------------------
        x,y=0,0
        print("    File Decoded\n\n    Initializing image generation...")

        try:
            image = Image.new('RGB', (m, n))                                # Creates a new image

            index = -1
            for x in range(m):
                for y in range(n):
                    index += 1

                    color = pixel_data[index]
                    image.putpixel((x, y), color)                           # Assigns colour to pixel using xy co-ordinate data
            print("    Image Generated succesfully")
        except Exception as e:
            print("\n[ERROR] Image Generation Failed")
            if Debug_mode:
                print(f"\n[ERROR] {e}")
            input()
            sys.exit()

        #---------------------- Image Enhancement & Upscaling ----------------------
        if enable_upscaling and upscale_factor > 1.0:
            print("\n    Applying advanced upscaling and enhancement...")
            try:
                image = Upscale_Image(image, upscale_factor)
            except Exception as e:
                print(f"    [WARNING] Upscaling failed: {e}")
                print("    Continuing with original image...")

        #---------------------- Saving Image ----------------------
        print("\n    Saving Image...")

        # Get just the filename without the path
        filename = os.path.basename(Encoded_img)
        if 'Encoded_' in filename:
            filename = filename.replace("Encoded_", "")
        
        # Add upscale indicator to filename
        base_name = filename[:-4]
        if enable_upscaling and upscale_factor > 1.0:
            save_filename = f'Decoded_Upscaled_{upscale_factor}x_{base_name}.jpg'
        else:
            save_filename = f'Decoded_{base_name}.jpg'
        
        try:
            
            if not os.path.exists("Decoded"):                               # If folder "Decoded" does not exist, then create it
                os.makedirs("Decoded")
            image.save(f'Decoded/{save_filename}')      # Saves the generated image with "Decoded_" prefix and the name of the txt file
        except Exception as e:
            print("\n[ERROR] Image saving failed")
            print(f"[ERROR] {e}")
            input()
            sys.exit()
        print("    Image saved successfully")
        try:
            os.startfile(f'Decoded/{save_filename}')            # Opens the saved image
        except:
            pass

        del image                                                           # Deleting un-used variables to save RAM

else:
    print("\n[ERROR] Please specify using 'E' and 'D' only")
    input()
    sys.exit()

if Debug_mode is True:
    end_time = time.perf_counter ()
    ao = (end_time - start_time)//1
    if ao>=60:
        ao = str(int(ao//60)) +" Min " + str(int(ao%60)) + " Sec"
    else:
        ao = str(int(ao)) + ' Sec'
    print(f"\nTime for execution : {ao}")                                   # Calculates and prints the time taken for execution of the program
    input()