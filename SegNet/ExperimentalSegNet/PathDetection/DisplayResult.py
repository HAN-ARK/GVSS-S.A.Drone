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
    final_frame_lists = []
    # final_frame = 0

    count = 1
    for input, output in zip(input_images, output_images):

        input_frame = cv2.imread(input, cv2.IMREAD_COLOR)
        output_frame = cv2.imread(output, cv2.IMREAD_COLOR)
        frame = cv2.hconcat([input_frame, output_frame])

        cv2.imshow("Picture{0}".format(count), frame)
        # cv2.imshow("input{0}".format(count), input_frame)
        # cv2.imshow("Output{0}".format(count), Mr. Robotoutput_frame)
        # final_frame_lists.append(frame)
        # final_frame = v_concat(frame, count)

        del(input_frame)
        del(output_frame)
        del(frame)

        count += 1

    #cv2.imshow("Final", final_frame)
    print(final_frame_lists)
    cv2.waitKey()
    cv2.destroyAllWindows()

# def v_concat(frame, count):
#     if count == 0:
#         return frame
#     elif count >= 1:
#         return cv2.vconcat(frame, v_concat(frame, count - 1))


if __name__ == '__main__':
    main()
