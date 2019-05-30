import CoDrone


def main():
    drone = CoDrone.CoDrone()
    drone.pair(drone.Nearest)

    # print current drone's trim value
    trim_info = drone.get_trim()

    drone.takeoff()

    drone.trim(-10, 0, 0, 0)
    print(trim_info.ROLL, trim_info.PITCH, trim_info.YAW, trim_info.THROTTLE)

    drone.hover(10)
    drone.land()

    drone.disconnect()


if __name__ == '__main__':
    main()
