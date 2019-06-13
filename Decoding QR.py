import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import CoDrone
from CoDrone import Direction,Degree

lowerBound=np.array([0,120,70])
upperBound=np.array([10,255,255])

lower = np.array([170,120,70])
upper = np.array([180,255,255])

cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))


#Function that gives movement commands to Drone based on QR input
def QR_to_commands(sCom):

    switcher = {
        
        #Turn right at specified degree
        "45 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_45),
        "60 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_60),
        "90 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_90),
        "120 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_120),
        "135 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_135),
        "150 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_150),
        "180 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_180),
        "210 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_210),
        "225 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_225),
        "240 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_240),
        "270 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_270),
        "300 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_300),
        "315 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_315),
        "330 RIGHT": drone.turn_degree(Direction.RIGHT, Degree.ANGLE_330),

        #Turn left at specified degree
        "45 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_45),
        "60 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_60),
        "90 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_90),
        "120 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_120),
        "135 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_135),
        "150 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_150),
        "180 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_180),
        "210 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_210),
        "225 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_225),
        "240 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_240),
        "270 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_270),
        "300 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_300),
        "315 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_315),
        "330 LEFT": drone.turn_degree(Direction.LEFT, Degree.ANGLE_330)

    }
    return switcher.get(argument)

#Video Feed Loop
while True:
    ret, img = cam.read()
    lestr = ""

    #QR code reader
    decodedImage = pyzbar.decode(img)
    for obj in decodedImage:

        #The decoded bytes are stored in this string variable
        lestr = obj.data.decode()

        #The string vairable issues a command to the drone
        #QR_to_commands(lestr)

    print (lestr)
    print (type(lestr))
    cv2.imshow("cam",img)
    cv2.waitKey(1)
