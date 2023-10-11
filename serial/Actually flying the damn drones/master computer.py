# Something like this this program is for the computer that will control both drones, through its own wifi and an
# existing computer REMEMBER!! - the serial connection should have the red part connected to this computer.
# and the purple to the other computer

import serial
import time

red_serial_port = "/dev/tty.usbserial-AH01H2QM"
purple_serial_port = "/dev/tty.usbserial-A9014EXK"

ser = serial.Serial(port=red_serial_port, baudrate=115200)

while True:
    ser.write("1".encode('utf-8')) # fly
    ser.write("\n".encode('utf-8'))
    time.sleep(5)
    ser.write("0".encode('utf-8')) # land
    ser.write("\n".encode('utf-8'))
    time.sleep(5)