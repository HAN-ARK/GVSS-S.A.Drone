import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar
import CoDrone
import threading
import time

#drone = CoDrone.CoDrone()
#drone.pair(drone.Nearest)
#drone.takeoff()

lowerBound=np.array([0,120,70])
upperBound=np.array([10,255,255])

lower = np.array([170,120,70])
upper = np.array([180,255,255])
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

#Capture video from the Wifi Connection to FPV module
#RTSP =(Real Time Streaming Protocol)
cam = cv2.VideoCapture('rtsp://192.168.100.1/cam1/mpeg4')
#cap = cv2.VideoCapture(0)

global index
index = 5

global csum
csum = 0

def mainThread():
    while True:
        global index
        global csum
        
        global img
        ret, img = cam.read()
        img = cv2.resize(img,(1113,720))

        #convert BGR to HSV
        imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        # create the Mask
        mask=cv2.inRange(imgHSV,lowerBound,upperBound)
        mask2 = cv2.inRange(imgHSV,lower,upper)
        mask = mask + mask2
        #morphology
        maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
        maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

        maskFinal=maskClose
        conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(img,conts,-1,(255,0,0),3)
        for i in range(len(conts)):
            x,y,w,h=cv2.boundingRect(conts[i])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)

        #drawing reference rectangle (where object must be)
        height = img.shape[0]
        width = img.shape[1]
        
        startrow, startcol = int(height/2)-300, int(width/2)-300
        endrow, endcol = int(height/2)-100, int(width/2)-100
        cropped = maskClose[startrow:endrow, startcol:endcol]
        cv2.rectangle(img, (int(width/2)-300,int(height/2)-300), (int(width/2)-100,int(height/2)-100), (255,0,0), 4)

        croppedsize = np.size(cropped)
        nonzero = np.count_nonzero(cropped)
        percent = 100*nonzero/croppedsize
        csum = percent
        #print(round(percent), end = " ")

        great = percent
        index = 1

        startrow, startcol = int(height/2)-300, int(width/2)-100
        endrow, endcol = int(height/2)-100, int(width/2)+100
        cropped2 = maskClose[startrow:endrow, startcol:endcol]
        cv2.rectangle(img, (int(width/2)-100,int(height/2)-300), (int(width/2)+100,int(height/2)-100), (255,0,0), 4)

        croppedsize = np.size(cropped2)
        nonzero = np.count_nonzero(cropped2)
        percent = 100*nonzero/croppedsize
        csum = csum + percent
        #print(round(percent), end = " ")

        if percent >= great:
            great = percent
            index = 2
        
        startrow, startcol = int(height/2)-300, int(width/2)+100
        endrow, endcol = int(height/2)-100, int(width/2)+300
        cropped3 = maskClose[startrow:endrow, startcol:endcol]
        cv2.rectangle(img, (int(width/2)+100,int(height/2)-300), (int(width/2)+300,int(height/2)-100), (255,0,0), 4)

        croppedsize = np.size(cropped3)
        nonzero = np.count_nonzero(cropped3)
        percent = 100*nonzero/croppedsize
        csum = csum + percent
        #print(round(percent), end = " ")

        if percent >= great:
            great = percent
            index = 3

        startrow, startcol = int(height/2)-100, int(width/2)-300
        endrow, endcol = int(height/2)+100, int(width/2)-100
        cropped4 = maskClose[startrow:endrow, startcol:endcol]
        cv2.rectangle(img, (int(width/2)-300,int(height/2)-100), (int(width/2)-100,int(height/2)+100), (255,0,0), 4)

        croppedsize = np.size(cropped4)
        nonzero = np.count_nonzero(cropped4)
        percent = 100*nonzero/croppedsize
        csum = csum + percent
        #print(round(percent), end = " ")

        if percent >= great:
            great = percent
            index = 4

        startrow, startcol = int(height/2)-100, int(width/2)-100
        endrow, endcol = int(height/2)+100, int(width/2)+100
        cropped5 = maskClose[startrow:endrow, startcol:endcol]
        cv2.rectangle(img, (int(width/2)-100,int(height/2)-100), (int(width/2)+100,int(height/2)+100), (255,0,0), 4)

        croppedsize = np.size(cropped5)
        nonzero = np.count_nonzero(cropped5)
        percent = 100*nonzero/croppedsize
        csum = csum + percent
        #print(round(percent), end = " ")

        if percent >= great:
            great = percent
            index = 5

        startrow, startcol = int(height/2)-100, int(width/2)+100
        endrow, endcol = int(height/2)+100, int(width/2)+300
        cropped6 = maskClose[startrow:endrow, startcol:endcol]
        cv2.rectangle(img, (int(width/2)+100,int(height/2)-100), (int(width/2)+300,int(height/2)+100), (255,0,0), 4)

        croppedsize = np.size(cropped6)
        nonzero = np.count_nonzero(cropped6)
        percent = 100*nonzero/croppedsize
        csum = csum + percent
        #print(round(percent), end = " ")

        if percent > great:
            great = percent
            index = 6

        startrow, startcol = int(height/2)+100, int(width/2)-300
        endrow, endcol = int(height/2)+300, int(width/2)-100
        cropped7 = maskClose[startrow:endrow, startcol:endcol]
        cv2.rectangle(img, (int(width/2)-300,int(height/2)+100), (int(width/2)-100,int(height/2)+300), (255,0,0), 4)

        croppedsize = np.size(cropped7)
        nonzero = np.count_nonzero(cropped7)
        percent = 100*nonzero/croppedsize
        csum = csum + percent
        #print(round(percent), end = " ")

        if percent > great:
            great = percent
            index = 7
        
        startrow, startcol = int(height/2)+100, int(width/2)-100
        endrow, endcol = int(height/2)+300, int(width/2)+100
        cropped8 = maskClose[startrow:endrow, startcol:endcol]
        cv2.rectangle(img, (int(width/2)-100,int(height/2)+100), (int(width/2)+100,int(height/2)+300), (255,0,0), 4)

        croppedsize = np.size(cropped8)
        nonzero = np.count_nonzero(cropped8)
        percent = 100*nonzero/croppedsize
        csum = csum + percent
        #print(round(percent), end = " ")

        if percent > great:
            great = percent
            index = 8
        
        startrow, startcol = int(height/2)+100, int(width/2)+100
        endrow, endcol = int(height/2)+300, int(width/2)+300
        cropped9 = maskClose[startrow:endrow, startcol:endcol]
        cv2.rectangle(img, (int(width/2)+100,int(height/2)+100), (int(width/2)+300,int(height/2)+300), (255,0,0), 4)

        croppedsize = np.size(cropped9)
        nonzero = np.count_nonzero(cropped9)
        percent = 100*nonzero/croppedsize
        csum = csum + percent
        #print(round(percent), end = " ")

        if percent > great:
            great = percent
            index = 9

        croppedsize = np.size(cropped5)
        nonzero = np.count_nonzero(cropped5)
        percent = 100*nonzero/croppedsize

        if percent > 80.0:
            cv2.rectangle(img, (int(width/2)-100,int(height/2)-100), (int(width/2)+100,int(height/2)+100), (0,255,0), 4)
        
        cv2.imshow("cam",img)
        cv2.waitKey(1)


def DroneMovement():
    count = 0
    while True:

        global index
        global csum
        global img

        findex = index
        fcsum = csum

        """def QR_to_commands(sCom):
            switcher = {                
                #Turn right at specified degree
                "45 RIGHT": print("Turn right 45 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_45),
                "60 RIGHT": print("Turn right 60 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_60),
                "90 RIGHT": print("Turn right 90 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_90),
                "120 RIGHT": print("Turn right 120 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_120),
                "135 RIGHT": print("Turn right 135 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_135),
                "150 RIGHT": print("Turn right 150 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_150),
                "180 RIGHT": print("Turn right 180 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_180),
                "210 RIGHT": print("Turn right 210 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_210),
                "225 RIGHT": print("Turn right 225 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_225),
                "240 RIGHT": print("Turn right 240 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_240),
                "270 RIGHT": print("Turn right 270 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_270),
                "300 RIGHT": print("Turn right 300 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_300),
                "315 RIGHT": print("Turn right 315 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_315),
                "330 RIGHT": print("Turn right 330 degrees"),#drone.turn_degree(Direction.RIGHT, Degree.ANGLE_330),

                #Turn left at specified degree
                "45 LEFT": print("Turn left 45 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_45),
                "60 LEFT": print("Turn left 60 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_60),
                "90 LEFT": print("Turn left 90 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_90),
                "120 LEFT": print("Turn left 120 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_120),
                "135 LEFT": print("Turn left 135 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_135),
                "150 LEFT": print("Turn left 150 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_150),
                "180 LEFT": print("Turn left 180 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_180),
                "210 LEFT": print("Turn left 210 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_210),
                "225 LEFT": print("Turn left 225 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_225),
                "240 LEFT": print("Turn left 240 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_240),
                "270 LEFT": print("Turn left 270 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_270),
                "300 LEFT": print("Turn left 300 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_300),
                "315 LEFT": print("Turn left 315 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_315),
                "330 LEFT": print("Turn left 330 degrees"),#drone.turn_degree(Direction.LEFT, Degree.ANGLE_330)
            }
            return switcher.get(argument, "No signal")"""

        if fcsum <= 20.0:
            print("Looking for Ballon")
            print(count)
            count = count + 1
            if count > 4:                
                """print("No ballon found, looking for QR code")
                #QR code reader
                decodedImage = pyzbar.decode(img)
                lestr = ""
                for obj in decodedImage:
                    #The decoded bytes are stored in this string variable
                    lestr = obj.data.decode()
                if lestr != "":                    
                    QR_to_commands(lestr)"""
                print("No ballon found, changing direction: turn right 90 degrees.")
            """drone.set_pitch(0)
            drone.set_roll(0)
            drone.set_throttle(0)"""
        elif fcsum <= 80.0:
            count = 0
            print("Go forwards")
            #drone.set_pitch(40)
            if findex < 4:
                print("Go up")
                #drone.set_throttle(40)
                if findex == 1:
                    print("Go left")
                    #drone.set_roll(-40)
                elif findex == 3:
                    print("Go right")
                    #drone.set_roll(40)
                else:
                    print("Stay centered")
                    #drone.set_roll(0)
            elif findex < 7:
                print("Keep altitude")
                #drone.set_throttle(0)
                if findex == 4:
                    print("Go left")
                    #drone.set_roll(-40)
                elif findex == 6:
                    print("Go right")
                    #drone.set_roll(40)
                else:
                    print("Stay Centered")
                    #drone.set_roll(0)
            else:
                print("Go down")
                #drone.set_throttle(-40)
                if findex == 7:
                    print("Go left")
                    #drone.set_roll(-40)
                elif findex == 9:
                    print("Go right")
                    #drone.set_roll(40)
                else:
                    print("Stay Centered")
                    #drone.set_roll(0)
        elif fcsum <= 500.0:
            count = 0
            print("Hover")
            """drone.set_pitch(0)
            drone.set_roll(0)
            drone.set_throttle(0)"""
        else:
            count = 0
            print("Go backwards")

        print("----------------------------------------------")
        #drone.move(3)
        time.sleep(3)

threadmainThread = threading.Thread(target=mainThread)
threadmainThread.start()


threadDroneMovement = threading.Thread(target=DroneMovement)
threadDroneMovement.start()
