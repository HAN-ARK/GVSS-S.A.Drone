#importing libraries
import CoDrone
import math
from CoDrone import Direction,Degree

import threading
import time

#creating objects + pairing
drone = CoDrone.CoDrone()
drone.pair(drone.Nearest)

#This function runs in a thread and constantly gets and outputs data from the
#opitcal flow sensor
def Drone_AntiDrift():
    
    state = drone.get_state()

    #Start of while loop
    while True:

        #Initialization of initial position object
        positionInitial = drone.get_opt_flow_position()

        time.sleep(1.5)

        #Initialization of final position object
        positionFinal = drone.get_opt_flow_position()

        #Horizontal Displacement
        positionDisplacementX = positionFinal.X - positionInitial.X

        #Vertical Displacment
        positionDisplacementY = positionFinal.Y - positionInitial.Y

        TotalDisplacementX = positionDisplacementX * positionDisplacementX

        TotalDisplacementY = positionDisplacementY * positionDisplacementY

        #The total distance that has been travelled along a diagonal line
        TotalDisplacement = math.sqrt(TotalDisplacementX + TotalDisplacementY)

        #Posistive horizontal displacement indicates movement to the right
        if positionDisplacementX > 0:

            DirectionX = "Right"

        #Negative horizontal displacement indicates movement to the left
        if positionDisplacementX < 0:

            DirectionX = "Left"

        
        #Positive vertical displacement indicates upwards movement        
        if positionDisplacementY > 0:

            DirectionY = "Up"


        #Negative vertical displacement indicates backwards movement
        #Should only occur if the drone comes to a sudden stop
        if positionDisplacementY < 0:

            DirectionY = "Down"


        #print (TotalDisplacement," ",DirectionX," ",DirectionY)

        print (DirectionX," ",positionDisplacementX,DirectionY," ",positionDisplacementY)

Drone_AntiDrift()

        

