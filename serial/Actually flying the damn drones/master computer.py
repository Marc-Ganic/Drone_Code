# Something like this this program is for the computer that will control both drones, through its own wifi
# and an existing computer
# REMEMBER!! - the serial connection should have the red part connected to this computer.
# and the purple to the other computer

import serial
import time
from djitellopy import Tello

red_serial_port = "/dev/tty.usbserial-AH01H2QM"
purple_serial_port = "/dev/tty.usbserial-A9014EXK"

#setup tello drone
tello = Tello()
tello.connect()

ser = serial.Serial(port=red_serial_port, baudrate=115200)

while True:
    ser.write("1".encode('utf-8')) # fly
    ser.write("\n".encode('utf-8'))
    tello.takeoff()
    time.sleep(5)
    ser.write("0".encode('utf-8')) # land
    ser.write("\n".encode('utf-8'))
    tello.land()
    time.sleep(5)