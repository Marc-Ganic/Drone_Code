import serial

red_serial_port = "/dev/tty.usbserial-AH01H2QM"
purple_serial_port = "/dev/tty.usbserial-A9014EXK"

# declare object
ser = serial.Serial(port=purple_serial_port, baudrate=115200)

while True:
    value= ser.readline()
    valueInstring=str(value, 'UTF8').strip()
    print(valueInstring)