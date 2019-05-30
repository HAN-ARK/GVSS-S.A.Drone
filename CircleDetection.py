import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    img = cv2.resize(img, (340, 220))

    shape = img
    gray_img = cv2.cvtColor(shape, cv2.COLOR_BGR2GRAY)
    cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 120,

                               param1=100, param2=30, minRadius=0, maxRadius=0)

    circles = np.uint16(np.around(circles))

    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(shape, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(shape, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow("HoughCirlces", shape)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    cv2.imshow("cam", img)
    cv2.waitKey(1)
