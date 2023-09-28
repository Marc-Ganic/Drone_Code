import serial
import time

ser = serial.Serial(port='/dev/tty.usbserial-AH01H2QM', baudrate=9600)

while True:
    ser.write(1)
    time.sleep(1)