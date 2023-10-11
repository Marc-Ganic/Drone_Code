# something like this


import serial
from djitellopy import Tello

red_serial_port = "/dev/tty.usbserial-AH01H2QM"
purple_serial_port = "/dev/tty.usbserial-A9014EXK"

#setup tello drone
tello = Tello()
tello.connect()

# declare object
ser = serial.Serial(port=purple_serial_port, baudrate=115200)

while True:
    value= ser.readline()
    valueInstring=str(value, 'UTF8').strip()
    print(valueInstring)
    if valueInstring == '1':
        tello.takeoff()
        print("Take off!")
    elif valueInstring == '0':
        tello.land()
        print("Land")