import serial

ser = serial.Serial(port='/dev/tty.usbserial-AH01H2QM', baudrate=9600)

while True:
    value= ser.readline()
    valueInstring=str(value, 'UTF8')
    print(valueInstring)