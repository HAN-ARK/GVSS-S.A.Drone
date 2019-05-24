import cv2
import numpy as np
#import CoDrone


def main():
    # Change this to your input device
    cap = cv2.VideoCapture('rtsp://192.168.100.1/cam1/mpeg4')
    rval = True
    num_image = 1  # Adjust this number to save desired amount of images
    cv2.namedWindow("Monitor")

    while rval:
        rval, frame = cap.read()

        if not rval:
            break

        cv2.imshow("Monitor", frame)

        key = cv2.waitKey(1)  # Checks for every 1 milisecond.
        """
            To take a screenshot, press t key.
            To stop this program, press q key.
        """
        if key == ord('t'):
            # The file will be saved as num_image.png
            cv2.imwrite("{0}.png".format(num_image), frame)
            num_image += 1
        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
