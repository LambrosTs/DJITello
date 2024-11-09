import cv2
from djitellopy import Tello
import time

drone = Tello()

# Connect to the drone and start streaming
drone.connect()
drone.streamon()

# Get the frame from the stream
while True:
    frame = drone.get_frame_read().frame
    cv2.imshow("Tello Camera Stream", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
drone.streamoff()
cv2.destroyAllWindows()
