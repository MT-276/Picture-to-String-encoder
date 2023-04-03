# Picture Encoder and Decoder
This Python script can encode any PNG or JPEG image with an additional layer of security by converting the pixel values into a hashed string that can be easily decoded. This code can be useful for concealing secret messages or data inside an image file that is difficult to detect.

# Getting Started
These instructions will help you to run this project on your local machine.

## Prerequisites
The script requires Python 3.x and several libraries to run, such as:

* PIL (Python Imaging Library)

### Installing
* Install Python 3.x from the official website: https://www.python.org/downloads/
Open the terminal or command prompt and enter the following command to install the required libraries:
Copy code
pip install Pillow
How to Use
Clone this repository or download the source code.
Open the terminal or command prompt and navigate to the directory where the script is located.
Run the following command to start the script:
Copy code
python picture-encoder-decoder.py
Follow the on-screen instructions to encode or decode the image.
Functionality
Encoding
The encoding process involves taking the RGB pixel values of an image and converting them into a hashed string. The resulting string can then be stored, shared, or transmitted with additional security since it would be hard for an attacker to decode the message. To encode an image, select the "E" option from the main menu and provide the path of the image file.

Decoding
To decode an encoded image, select the "D" option from the main menu and enter the hashed string. The script will then convert the hashed string back into its original RGB pixel values and display the decoded image on the screen.

Notes
The script only works with PNG or JPEG image files. If the input image is in a different format, it will be converted to PNG format automatically.
The script uses a custom hashing algorithm that converts each pixel value into a combination of letters and symbols. The algorithm is not cryptographically secure, so it should not be used for sensitive data.
This project is not intended to be used for illegal or unethical purposes. The developer assumes no liability for any misuse of the script.
