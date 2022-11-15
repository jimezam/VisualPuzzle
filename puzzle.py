# $ python3 -m venv env
# $ source env/bin/activate
# $ pip install opencv-contrib-python numpy

import cv2 as cv2
import numpy as np

rows = 3
cols = 4

image = cv2.imread('assets/image-1.jpg')

height, width, channels = image.shape

boxWidth = int(width / cols)
boxHeight = int(height / rows)

imageParts = np.zeros((rows, cols))

numRows = np.shape(imageParts)[0]
numColumns = np.shape(imageParts)[1]

for r in range(numRows):
    for c in range(numColumns):
        rx = r * boxHeight
        cx = c * boxWidth
  
        imageParts[r, c] = image[rx:rx+boxHeight, cx:cx+boxWidth]
        # cv2.imshow(f"{r}x{c}", image[rx:rx+boxHeight, cx:cx+boxWidth])  

cv2.waitKey(0)  
cv2.destroyAllWindows()