import cv2
import numpy as np

#Capture the video from my computer's Web cam.
cap = cv2.VideoCapture(0)

while True:
    
    #Put the captured video under the variable 'frame' per loop 
    _, frame = cap.read()
    
    #Convert the video to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Using the laplacian method
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    
    #Using sobel method to enhance the gradients of the HSV image HORIZONTALLY
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    
    #Using sobel method to enhance the gradients of the HSV image VERTICALLY
    sobely = cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    
    #Using the Canny method to show the edge in a clear way.
    canny = cv2.Canny(frame, 100, 150)
    
    #Show the video of these methods
    cv2.imshow('Original frame',frame)
    
    cv2.imshow("sobelx", sobelx)
    
    cv2.imshow("sobely", sobely)
    
    cv2.imshow("Laplacian", laplacian)
    
    cv2.imshow("Canny", canny)
    
    #Quit the program Using the Escape key.
    key = cv2.waitKey(1)
    if key == 27:
        break

# The program finishes
cap.release()
cv2.destroyAllWindows()
