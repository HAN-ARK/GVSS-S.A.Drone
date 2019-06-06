import cv2
import numpy as np

cap = cv2.VideoCapture('rtsp://192.168.100.1/cam1/mpeg4')

rval = True
count = 1

while rval:
    rval, frame = cap.read()

    if not rval:
        break
    cv2.imshow("Display", frame)

    key = cv2.waitKey(1)
    if key == 27:  # exit on ESC
        break
    elif key == ord('q') or key == 65:
        cv2.imwrite(
            "/home/decuple/Development/Python_Project/GVSS-S.A.Drone/Train/TrainData/image{0}.jpg".format(count), frame)
        count += 1

cap.release()
cv2.destroyAllWindows()
