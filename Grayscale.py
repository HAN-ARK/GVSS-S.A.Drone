import cv2
import numpy as np

#Capture the video from my computer's Web cam.
cap = cv2.VideoCapture(0)

while True:
    
    #Put the captured video under the variable 'frame' per loop 
    _, frame = cap.read()
    
    #Convert the video to HSV
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Flip the camera
    frame_f = cv2.flip(frame, 1)
    
    #Smooth the image by GaussianBlur
    #For each pixel, a 5x5 window is centered on this pixel, 
    #all pixels falling within this window are summed up, and the result is then divided by 25. 
    blurred_frame = cv2.GaussianBlur(frame_f, (5, 5), 0)
    
    #Using the laplacian method
    laplacian = cv2.Laplacian(blurred_frame, cv2.CV_64F)
    
    #Using the Canny method to show the edge in a clear way.
    canny = cv2.Canny(blurred_frame, 100, 150)
    
    #Show the video of these methods
    cv2.imshow("Frame", frame_f)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Canny", canny)
    
    #Quit the program Using the Escape key.
    key = cv2.waitKey(1)
    if key == 27:
        break

# The program finishes   
cap.release()
cv2.destroyAllWindows()
