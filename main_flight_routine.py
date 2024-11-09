from djitellopy import tello

drone = tello.Tello()

drone.connect()
drone.takeoff()
drone.rotate_clockwise(360)
drone.land()
drone.end()

