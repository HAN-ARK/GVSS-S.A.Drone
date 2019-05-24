import CoDrone
import cv2
import numpy
import scipy
import time

def main():
    s = True
    rval = True

    #cv2.namedWindow('DelayFix')
    while s:
        cap = cv2.VideoCapture('rtsp://192.168.100.1/cam1/mpeg4')
        rval, frame = cap.read()

        if not rval:
            print("Could not connect to camera")
            break

        print("Connected")
        start = time.time()
        cv2.imshow("DelayFix", frame)

        cap.release
        print("Disconnected")
        end = time.time()
        print("Delay is {}".format(end - start) * 1000000)
        #time.sleep(3)

        del(frame)
        del(rval)
        del(cap)

if __name__ == "__main__":
    main()
