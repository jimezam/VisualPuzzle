import cv2 as cv2
import numpy as np

################################################################


def prepare(rows, cols, image):
    image = cv2.imread(image)

    height, width, channels = image.shape

    boxWidth = int(width / cols)
    boxHeight = int(height / rows)

    # numRows = np.shape(imageParts)[0]
    # numColumns = np.shape(imageParts)[1]

    imageMatrix = np.empty((rows, cols), np.ndarray)

    for r in range(rows):
        for c in range(cols):
            rx = r * boxHeight
            cx = c * boxWidth

            imageMatrix[r][c] = image[rx:rx+boxHeight, cx:cx+boxWidth]
            # cv2.imshow(f"{r}x{c}", imageMatrix[r][c])

    return imageMatrix

################################################################

def process(frame, qcd, decodedColor, errorColor, font):
    

    success_qr, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(frame)

    # print(points)

    if success_qr:
        for qr_data, qr_points in zip(decoded_info, points):
            color = decodedColor if qr_data else errorColor

            frame = cv2.polylines(frame, [qr_points.astype(int)], True, color, 8)
            ## TODO: check
            frame = cv2.putText(frame, qr_data, (50, 50), font, 3, (255, 0, 0), 3)

    return frame

################################################################
