#coffeepanda0
#improvements by JezzaProto

import argparse, os, sys
from math import sqrt, floor
try:
	from PIL import Image, ImageEnhance, ImageFont, ImageDraw
except ImportError:
	print("Pillow needs to be installed to run this program.")
	i = input("Would you like to try and install pillow? (y/n)")
	if i.lower() == "y" or i.lower() == "yes":
		os.system("pip install pillow")
		os.system("python -m pip install pillow")
		os.system("py -m pip install pillow")
		try:
			from PIL import Image, ImageEnhance
		except ImportError:
			print("Failed to install Pillow. Please do this manually.")
			sys.exit()
	else:
		print("Quitting")
		sys.exit()

width, height = 0,0

def chars(brightness):
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

def work(bright, image):
	row, col = 0,1
	if bright != 1:
		enhancer = ImageEnhance.Brightness(image)
		image = enhancer.enhance(bright)
	for _ in range(1, height):
		while row < width -1:
			row += 1
			r, g, b = image.getpixel((row, col))
			brightness = sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
			chars(brightness)
			chars(brightness)
		row = 0
		col += 1
		file.write("\n")

	print(f"Success! Outputted to {file.name}")
	file.close()

def main():
	global file, image, width, height, fpath

	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('image', nargs="?", help='The file to convert to ascii', default="none")
	parser.add_argument('-o', nargs="?", help='The text file to output to.', default="none", type=str, dest="output")
	parser.add_argument("-b", nargs="?", help="How much to multiply the brightness by", default=1, type=float, dest="bright")
	parser.add_argument("-c", nargs="?", help="Compress the image and specify new size for a smaller output (e.g -c  800,200)", type=str, dest="dimensions")
	parser.add_argument("-r", nargs="?", help="Compress and keep ratio the same (Specify scale to compress by)", default=1, type=float, dest="ratio")
	parser.add_argument("-m", nargs="?", help="Max number of characters that the output can have (Auto-scaling)", default=1, type=int, dest="chars")
	parser.add_argument("-t", nargs="*", help="Text to convert into ascii art", default="none", type=str, dest="text")
	args = parser.parse_args()
	fpath = args.image
	output = args.output
	brightness = args.bright
	dimensions = args.dimensions
	compression = args.ratio
	chars = args.chars
	text = " ".join(args.text)
	
	if output == "none":
		if fpath == "none":
			output = "output.txt"
		else:
			output = fpath.split(os.path.sep)[-1]
			output = output.split(".")[0:-1]
			output = ".".join(output)
			output += ".txt"

	file = open(output,"w")
	
	if text != "n o n e":
		font = ImageFont.truetype("arial.ttf", 98)
		background = Image.new("RGB", (2000,2000), (255,255,255))
		draw = ImageDraw.Draw(background)
		twidth, theight = draw.textsize(text, font=font)
		draw.text((0,0), text, font=font, fill="black")
		background = background.crop((0, 0, twidth, theight))
		image = background
		width = twidth
		height = theight
		if dimensions is not None:
			if compression != 1:
				print("You can't specify dimensions and compress by a ratio. Use ether just ratio (-r) or just dimensions (-c)")
				sys.exit()
			if chars != 1:
				print("You can't specify dimensions and use auto-scaling. Use ether just ratio (-r) or just auto-scaling (-m)")
				sys.exit()
			try:
				dims = [int(i) for i  in dimensions.split(",")]
				comp_width = dims[0]
				comp_height = dims[1]
			except:
				print("Error, the dimensions specified are invalid")
				sys.exit()
		
		if chars != 1:
			if compression != 1:
				print("You can't specify auto-scaling and compress by a ratio. Use ether just auto-scaling (-m) or just a ratio (-r)")
				sys.exit()
			width, height = image.size
			image_size = (width*2) * height
			while image_size >= chars:
				width *= 0.99
				height *= 0.99
				image_size = (width*2) * height
			width = floor(width)
			height = floor(height)
			image = image.resize((width, height),box=None)
			work(brightness, image)
			sys.exit()
		work(brightness, image)
		sys.exit()

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
	if dimensions is not None:
		if compression != 1:
			print("You can't specify dimensions and compress by a ratio. Use ether just ratio (-r) or just dimensions (-c)")
			sys.exit()
		if chars != 1:
			print("You can't specify dimensions and use auto-scaling. Use ether just ratio (-r) or just auto-scaling (-m)")
			sys.exit()
		try:
			dims = [int(i) for i  in dimensions.split(",")]
			comp_width = dims[0]
			comp_height = dims[1]
		except:
			print("Error, the dimensions specified are invalid")
			sys.exit()
	
	if chars != 1:
		if compression != 1:
			print("You can't specify auto-scaling and compress by a ratio. Use ether just auto-scaling (-m) or just a ratio (-r)")
			sys.exit()
		width, height = image.size
		image_size = (width*2) * height
		while image_size >= chars:
			width *= 0.99
			height *= 0.99
			image_size = (width*2) * height
		width = floor(width)
		height = floor(height)
		image = image.resize((width, height),box=None)
		work(brightness, image)
		sys.exit()

	width, height = image.size
	comp_width = int(round(width / compression))
	comp_height = int(round(height / compression))
	image = image.resize((comp_width, comp_height),box=None)
	width, height = image.size
	work(brightness, image)

if __name__ == "__main__":
   main()
