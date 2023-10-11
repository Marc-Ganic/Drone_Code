import serial
import time

red_serial_port = "/dev/tty.usbserial-AH01H2QM"
purple_serial_port = "/dev/tty.usbserial-A9014EXK"

ser = serial.Serial(port=red_serial_port, baudrate=115200)

while True:
    ser.write("Mads kan godt lide pik".encode('utf-8'))
    ser.write("\n".encode('utf-8'))
    time.sleep(1)