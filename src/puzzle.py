import cv2 as cv2
import numpy as np

def prepare(rows, cols, image):
    image = cv2.imread(image)

    height, width, channels = image.shape

    boxWidth = int(width / cols)
    boxHeight = int(height / rows)

    imageParts = np.zeros((rows, cols))

    numRows = np.shape(imageParts)[0]
    numColumns = np.shape(imageParts)[1]

    imageMatrix = np.empty((numRows, numColumns), np.ndarray)

    for r in range(numRows):
        for c in range(numColumns):
            rx = r * boxHeight
            cx = c * boxWidth
    
            imageMatrix[r][c] = image[rx:rx+boxHeight, cx:cx+boxWidth]
            # cv2.imshow(f"{r}x{c}", imageMatrix[r][c])  

    return imageMatrix