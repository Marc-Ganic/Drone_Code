import serial

ser = serial.Serial(port='/dev/tty.usbserial-AH01H2QM', baudrate=9600)

while True:
    ser.write("Hello world!")
    sleep(1)