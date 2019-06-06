import CoDrone
import numpy as np
import time

def main():
    drone = CoDrone.CoDrone()
    drone.pair(drone.Nearest)
    while True:
        angles = drone.get_gyro_angles()
        R = angles.ROLL
        P = angles.PITCH
        print("""
R: {0}
P: {1}
        """.format(R, P))

        time.sleep(2)


if __name__ == "__main__":
    main()
