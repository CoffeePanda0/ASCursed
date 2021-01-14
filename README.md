# ASCursed
cursed image to ASCII generator made in python

  converts each pixel in an image file to an ascii character so when you zoom out on notepad it looks epic ~~and does not take a long time to run~~

 ![](https://cdn.discordapp.com/attachments/423207516663709708/772258930453119026/unknown.png)
 
 
this was written in less than 2 hours and is a mess

# Requirements
- Python 3.4 or higher
- PIL
- A stable mental state

# Usage
usage: ascii.py [-h] [-o [OUTPUT]] [-b [BRIGHT]] [-c [COMPRESSION]] [-r [RATIO]] [-m [MAX CHARS]] [-t [TEXT]] image

(-h, -o, -c, -r, -m, -t and -b are not needed to run). If -o is not specified, ascii.py will output to the file name + .txt

With -c specify the new width and height for the output (e.g -c 1920,1080)

With -r specify the ratio (e.g -r 5) makes the image 5 times smaller with the same height:width ratio as before

With -m specify the max number of characters

Example:
python3 ascii.py -o duck.txt duck.png

Supports the vast majority of image formats
