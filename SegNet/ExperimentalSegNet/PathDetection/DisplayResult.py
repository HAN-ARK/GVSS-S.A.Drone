"""
    Author: HB
    Description: This program shows the results of segnet
    Date: May 15, 2019
"""

import glob
import cv2


def main():
    input_images = glob.glob(
        '/home/decuple/Development/Python_Project/GVSS-S.A.Drone/SegNet/ExperimentalSegNet/PathDetection/Input/*.png')
    output_images = glob.glob(
        '/home/decuple/Development/Python_Project/GVSS-S.A.Drone/SegNet/ExperimentalSegNet/PathDetection/Output/*.png')

    input_images.sort()
    output_images.sort()

    count = 1
    for input, output in zip(input_images, output_images):

        input_frame = cv2.imread(input, cv2.IMREAD_COLOR)
        output_frame = cv2.imread(output, cv2.IMREAD_COLOR)

        cv2.imshow("input{0}".format(count), input_frame)
        cv2.imshow("Output{0}".format(count), output_frame)

        del(input_frame)
        del(output_frame)

        count += 1

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
