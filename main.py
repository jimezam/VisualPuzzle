# $ pip install opencv-contrib-python numpy

import cv2 as cv2
import numpy as np
import src.puzzle as puzzle

################################################################

def main():
    rows = 3
    cols = 4

    imageMatrix = puzzle.prepare(rows, cols, 'assets/image-1.jpg')

    # ...

    cv2.waitKey(0)  
    cv2.destroyAllWindows()

################################################################

if __name__ == '__main__':
    main()

################################################################