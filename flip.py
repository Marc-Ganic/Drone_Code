from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()

tello.takeoff()

for i in range(2):
    tello.move_up(500)

tello.emergency()




tello.flip_forward()
tello.flip_back()


tello.land()