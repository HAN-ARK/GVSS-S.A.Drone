import cv2 
import numpy as np

###
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
        crop = image[balloon[1]-balloon[2]:balloon[1]+balloon[2],balloon[0]-balloon[2]:balloon[0]+balloon[2]]
        return crop 
###

video = cv2.VideoCapture(0)     

_, first_frame = video.read()                                     

balloon_roi = getBalloonImage(first_frame)                   
h, w,chnls = balloon_roi.shape
#print (h,w)

x = 0
y = 0
width = w
height = h
roi = balloon_roi[y: y + height, x: x + width] 

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
#print(roi_hist)

term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)     

#cap = cv2.VideoCapture(0)
frameNum = 0 

cv2.imshow("roi", roi)

while True:          
    
    _, frame = video.read()#cap
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    
    mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
	
    _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)   
    #print(track_window)
    x, y, w, h = track_window
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
    cv2.imshow("Mask", mask)
    #cv2.imshow("First frame", first_frame)
    cv2.imshow("Frame", frame)
    frameNum = frameNum + 1
    key = cv2.waitKey(10)
    if key == 32:
	    break
		
video.release()
cv2.destroyAllWindows()
