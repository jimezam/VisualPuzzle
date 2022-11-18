# $ pip install opencv-contrib-python numpy

import cv2 as cv2
import numpy as np
import src.puzzle as puzzle

################################################################

def main():
    rows = 3
    cols = 4

    imageMatrix = puzzle.prepare(rows, cols, 'assets/image-1.jpg')

    #################################################
    camera_id = 0
    cap = cv2.VideoCapture(camera_id)
    qcd = cv2.QRCodeDetector()
    decodedColor = (0, 255, 0)
    errorColor = (0, 0, 255)

    delay = 1
    windowName = 'Visual Puzzle'
    font = cv2.FONT_HERSHEY_PLAIN

    while True:
        success, frame = cap.read()

        if not success:
            continue

        processedFrame = puzzle.process(frame, qcd, decodedColor, errorColor, font)

        cv2.imshow(windowName, processedFrame)

        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    # cv2.destroyWindow(window_name)
    #################################################

    # cv2.waitKey(0)  
    cv2.destroyAllWindows()

################################################################

if __name__ == '__main__':
    main()

################################################################