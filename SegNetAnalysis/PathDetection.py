"""
    Author: Hanbyul Park
    Purpose: To detect the path from the result file of the SegNet model.
    Date: May 11, 2019
"""

import cv2
import numpy as np
import matplotlib


def main():
     imgfile = 'Segnetimage.png'
     img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

     cv2.namedWindow('Model', cv2.WINDOW_NORMAL)
     cv2.imshow('Model', img)

     cv2.waitKey(0)
     cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
