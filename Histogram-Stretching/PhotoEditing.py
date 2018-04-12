import numpy as np
from PIL import ImageEnhance 
from PIL import Image 

# img = cv2.imread('earthObs/ISS039-E-831.JPG',0)
# equ = cv2.equalizeHist(img)
# res = np.hstack((img,equ)) #stacking images side-by-side
# cv2.imwrite('equalized.jpg',equ)

image = Image.open('earthObs/ISS037-E-2163.jpg')
enhancer = ImageEnhance.Sharpness(image)
enhancer.enhance(1.8).show()
enhancer2 = ImageEnhance.Contrast(image)
enhancer2.enhance(2).show()