"""
    Author: Hanbyul Park
    Description: Modified version of demo
    Date: May 8, 2019
"""

import caffe
import numpy as np
import matplotlib.pyplot as plt
import os.path
import scipy
import argparse
import math
import cv29
import sys
import time

sys.path.append('/home/decuple/anaconda3/site-packages')
# The path of installed python libraries
# Make sure that caffe is on the python path:
caffe_root = '/usr/local/'
sys.path.insert(0, caffe_root + 'python')


# Import arguments
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, required=True)
parser.add_argument('--weights', type=str, required=True)
parser.add_argument('--colours', type=str, required=True)
args = parser.parse_args()


net = caffe.Net(args.model,
                args.weights,
                caffe.TEST)


caffe.set_mode_gpu()
input_shape = net.blobs['data'].data.shape
output_shape = net.blobs['argmax'].data.shape

label_colours = cv2.imread(args.colours).astype(np.uint8)

cv2.namedWindow("Input")
cv2.namedWindow("SegNet")

# cap = cv2.VideoCapture('rtsp://192.168.100.1/cam1/mpeg4')
# cap = cv2.VideoCapture(0) # Change this to your webcam ID, or file name for your video file


def SegNetData():
    '''
        Purpose: This function gets the image for every one second
    '''
    image_number = int(input("Which picture? : "))
    # imgfile = '/SegNet/Scripts/1.jpg'
    imgfile = '/SegNet/Scripts/{}.jpg'.format(image_number)
    frame = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    frame = cv2.resize(frame, (input_shape[3], input_shape[2]))
    input_image = frame.transpose((2, 0, 1))

    input_image = np.asarray([input_image])
    out = net.forward_all(data=input_image)

    segmentation_ind = np.squeeze(net.blobs['argmax'].data)
    segmentation_ind_3ch = np.resize(
        segmentation_ind, (3, input_shape[2], input_shape[3]))

    segmentation_ind_3ch = segmentation_ind_3ch.transpose(
        1, 2, 0).astype(np.uint8)
    segmentation_rgb = np.zeros(segmentation_ind_3ch.shape, dtype=np.uint8)

    cv2.LUT(segmentation_ind_3ch, label_colours, segmentation_rgb)
    # segmentation_rgb = segmentation_rgb.astype(float) / 255

    img_gray = cv2.cvtColor(segmentation_rgb, cv2.COLOR_BGR2GRAY)
    # roi = segmentation_rgb[0:224, 102:122]
    ret, img_binay_path = cv2.threshold(
        img_gray, 114, 255, cv2.THRESH_BINARY_INV)
    ret1, img_binay_path2 = cv2.threshold(
        img_gray, 115, 255, cv2.THRESH_BINARY_INV)
    diff = cv2.absdiff(img_binay_path, img_binay_path2)
    # cv2.absdiff

    # cv2.namedWindow('Binalization')
    # cv2.createTrackbar('threshold', "Binalization", 0, 255, nothing)
    # cv2.setTrackbarPos('threshold', 'Binalization', 127)

    cv2.imshow("Input", frame)
    cv2.imshow("SegNet", segmentation_rgb)
    # cv2.imshow("ROI", roi)
    cv2.imshow("Path", diff)

    height, width, channel = segmentation_rgb.shape
    print(
        """
Image Information
Height  : {0}
Width   : {1}
Channel : {2}
""".format(height, width, channel))
# 114 115 threshold
    """
    while(True):
        low = cv2.getTrackbarPos('threshold', 'Binalization')
        ret, img_binary = cv2.threshold(
            img_gray, low, 255, cv2.THRESH_BINARY_INV)

        cv2.imshow("Binalization", img_binary)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    """
    cv2.waitKey(0)
    cv2.imwrite("/home/decuple/Development/Python_Project/GVSS-S.A.Drone/SegNet/ExperimentalSegNet/PathDetection/Output/r{}.png".format(image_number), diff)
    cv2.imwrite("/home/decuple/Development/Python_Project/GVSS-S.A.Drone/SegNet/ExperimentalSegNet/PathDetection/Input/{}.png".format(image_number), frame)
    cv2.destroyAllWindows()


def nothing(x):
    pass


# def ToGrayScale(frame):
#     gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#     ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    # return dst


if __name__ == '__main__':
    SegNetData()
