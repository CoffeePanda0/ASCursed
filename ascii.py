#coffeepanda0

from PIL import Image
from math import sqrt
import os.path

fpath = "" # ENTER YOUR IMAGE FILE PATH HERE

file = open("output.txt","w") 

print("GREET TINGs!")

if os.path.isfile(fpath):
    try:
        image = Image.open(fpath)
        image = image.convert ('RGB')
    except:
        print("The file specified could not be opened as an image")
else:
        print("Error, image does not exist")

width, height = image.size

row = 1
col = 1
brightness = 0

def chars():
    if brightness < 25:
        file.write("@")
    elif brightness > 25 and brightness <= 50:
        file.write("0")
    elif brightness > 50 and brightness <= 75:
        file.write("O")
    elif brightness > 75 and brightness <= 100:
        file.write("d")
    elif brightness > 100 and brightness <= 125:
        file.write("a")
    elif brightness > 125 and brightness <= 150:
        file.write("o")
    elif brightness > 150 and brightness <= 200:
        file.write(".")
    elif brightness > 200 and brightness <= 225:
        file.write("*")
    else:
        file.write("'")

for x in range (1, height):
    while row < width -1:
            row += 1
            r, g, b = image.getpixel((row, col))
            brightness = sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
            chars()
    row = 0
    col += 1
    file.write("\n")
file.close() 