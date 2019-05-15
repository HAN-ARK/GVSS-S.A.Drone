import cv2 
import numpy as np

def findBalloonCentre(image):
    cimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image2 = cv2.medianBlur(cimage,7)
    circles = cv2.HoughCircles(image2,cv2.HOUGH_GRADIENT,1,120, param1=100,param2=30,minRadius=60,maxRadius=200)
    if circles is None:
        return 'BALLOON DETECTION FAILED!'
    else:
        circles = np.uint16(np.around(circles))   
        return  (circles[0, 0])
###

###
def getBalloonImage(image):
    balloon = findBalloonCentre(image)
    if balloon == 'BALLOON DETECTION FAILED!':
        print ('BALLOON DETECTION FAILED!')
        return 'BALLOON DETECTION FAILED!'
    else:
        h,w,channels = image.shape
        crop = image[balloon[1]-balloon[2]//2:balloon[1]+balloon[2]//2,balloon[0]-balloon[2]//2:balloon[0]+balloon[2]//2]
        return crop

def getDominantColor(image):
    avg_color_per_row = np.average(image, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    print(avg_color)
    return avg_color
	
video = cv2.VideoCapture('balloon2.avi')  

_, first_frame = video.read()

balloon = getBalloonImage(first_frame)     

getDominantColor(balloon)
cv2.imshow("Frame", balloon)
key = cv2.waitKey(10000)
cv2.destroyAllWindows()
