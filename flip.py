from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()

tello.takeoff()


tello.flip_forward()
tello.flip_back()


tello.land()