#coffeepanda0
#improvements by JezzaProto

import argparse, os, sys
from math import sqrt
try:
	from PIL import Image, ImageEnhance
except ImportError:
	print("Pillow needs to be installed to run this program.\nAttempting to install from pip.")
	os.system("pip install pillow")
	os.system("python -m pip install pillow")
	os.system("py -m pip install pillow")
	try:
		from PIL import Image
	except ImportError:
		print("Failed to install Pillow. Please do this manually.")
		os._exit(1)

width, height = 0,0

brightness = 0

def chars():
	global file
	if brightness < 25:
		file.write("@")
	elif brightness > 25 and brightness <= 50:
		file.write("0")
	elif brightness > 50 and brightness <= 75:
		file.write("O")
	elif brightness > 75 and brightness <= 90:
		file.write("B")
	elif brightness > 90 and brightness <= 100:
		file.write("d")
	elif brightness > 100 and brightness <= 125:
		file.write("a")
	elif brightness > 125 and brightness <= 135:
		file.write("q")
	elif brightness > 135 and brightness <= 150:
		file.write("o")
	elif brightness > 150 and brightness <= 175:
		file.write("c")
	elif brightness > 175 and brightness <= 200:
		file.write(".")
	elif brightness > 200 and brightness <= 225:
		file.write("*")
	else:
		file.write(" ")

def work(bright):
	row, col = 1,1
	global brightness, image
	if bright != 1:
		enhancer = ImageEnhance.Brightness(image)
		image = enhancer.enhance(bright)
	for x in range(1, height):
		while row < width -1:
				row += 1
				r, g, b = image.getpixel((row, col))
				brightness = sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
				chars()
		row = 0
		col += 1
		file.write("\n")
	print(f"Success! Outputted to {file.name}")
	file.close()

def main():
	global file, image, width, height, fpath

	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('image', help='The file to convert to ascii')
	parser.add_argument('-o', nargs="?", help='The text file to output to.', default="output.txt", type=str, dest="output")
	parser.add_argument("-b", nargs="?", help="How much to multiply the brightness by", default=1, type=float, dest="bright")

	args = parser.parse_args()
	fpath = args.image
	output = args.output
	brightness = args.bright

	print("GREET TINGs!")
	file = open(output,"w")

	if os.path.isfile(fpath):
		try:
			image = Image.open(fpath)
			image = image.convert('RGB')
		except:
			print("The file specified could not be opened as an image")
			sys.exit()
	else:
			print("Error, image does not exist")
			sys.exit()
	width, height = image.size
	work(brightness)

if __name__ == "__main__":
   main()
