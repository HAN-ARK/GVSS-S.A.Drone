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
def Drone_AntiDrift ():

    state = drone.get_state()

    #Start of while loop
    while (state == 'FLIGHT'):

        #Initialization of initial position object
        positionInitial = drone.get_opt_flow_position()

        time.sleep(3.0)

        #Initialization of final position object
        posistionFinal = drone.get_opt_flow_posistion()

        #Horizontal Displacement
        posistionDisplacementX = poisistionFinal.X - posistionInitial.X

        #Vertical Displacment
        posistionDisplacementY = posistionFinal.Y - posisitionInitial.Y

        TotalDisplacementX = posistionDisplacement.X * posistionDisplacement.X

        TotalDisplacementY = posistionDisplacement.Y * posistionDisplacemnet.Y

        #The total distance that has been travelled along a diagonal line
        TotalDisplacement = math.sqrt(TotalDisplacementX + TotalDisplacementY)

        #Posistive horizontal displacement indicates movement to the right
        if posistionDisplacementX > 0:

            DirectionX = "Right"

        #Negative horizontal displacement indicates movement to the left
        if posistionDisplacementX < 0:

            DirectionX = "Left"

        
        #Positive vertical displacement indicates upwards movement        
        if posistionDisplacementY > 0:

            DirectionY = "Up"


        #Negative vertical displacement indicates backwards movement
        #Should only occur if the drone comes to a sudden stop
        if posistionDisplacementY < 0:

            DirectionY = "Down"
