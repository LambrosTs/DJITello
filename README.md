# DJITello
Python programming the drone to do things like flight routine and stuff

Prerequisites: The computer must have a wireless network so to be able to connect to the drone. You have to install "djitellopy" and import tello so you can use the commands.

My computer: Wireless network card, Visual Studio Code, Windows 11.

DJITello restrictions: Tello's IMU sensor isn't known for the fast processing of data it receives, so many times my Tello executed a part of the code then it stand still for a while
and then it landed. To overpass that I imported time and now and then I use time.sleep(seconds) so it will take a brake for 2-5 seconds and give the IMU the time to proccess
data. You will not need this addition if your drone has a strong IMU sensor.

-- The main_flight_routine.py is a file with main commands on how to give orders so the drone execute them.

There are many commands to work on already on the library. For example if you write on VSCode drone.move -> it will open a lot o commands to choose.

--  The stream.py is a code so the drone will give you a visual of what its camera looking at on your pc screen.

** Whats do we need for the stream to work:
  -- We have to import cv2 (OpenCV library for computer vision and image processing tasks python)
  The specific purpose of cv2 in this code is to display the real-time video feed from the drone on the screen.

Caution: When I try to integrade the stream code into other codes for example the main_flight_routine.py it didn't work and I had to use defs!

More codes with funny stuff are coming up. Now I am working on tracking a face and use hand commands to drone.
