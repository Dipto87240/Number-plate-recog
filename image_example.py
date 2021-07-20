from PIL import Image
import pytesseract
import sys
import os.path

im = Image.open("test88.jpg")

text = pytesseract.image_to_string(im, lang = 'eng')

directory = 'Z:\Criminal_Number_Plate'

filename = "Day21March"+'.txt'
file_path = os.path.join(directory, filename)
if not os.path.isdir(directory):
    os.mkdir(directory)
file = open(file_path, "w")
file.write(text)
file.close()
print(text)




