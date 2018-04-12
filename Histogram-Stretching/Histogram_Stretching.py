from PIL import Image
from PIL import ImageEnhance
import operator

images = ["ISS036-E-34462.JPG", "ISS036-E-34506 (1).JPG", "ISS037-E-2163.JPG", "ISS039-E-831.JPG", "ISS040-E-105478.JPG"]

def equalize(im):
    h = im.convert("L").histogram()
    lut = []
    for b in range(0, len(h), 256):
        # step size
        step = reduce(operator.add, h[b:b+256]) / 255
        # create equalization lookup table
        n = 0
        for i in range(256):
            lut.append(n / step)
            n = n + h[i+b]
    # map image through lookup table
    return im.point(lut*im.layers)

for image in images: 
	im = Image.open(image)
	im.show() 
	im2 = equalize(im)
	im2.show() 