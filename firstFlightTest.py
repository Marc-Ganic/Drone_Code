from djitellopy import Tello

import logging #Kilde til logs, https://www.studytonight.com/python/python-logging-in-file

logging.basicConfig(filename='flight.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This message will get logged on to a file')

tello = Tello()

tello.connect()
tello.takeoff()


tello.move_left(100)
tello.rotate_clockwise(90)
tello.move_forward(100)

tello.land()
