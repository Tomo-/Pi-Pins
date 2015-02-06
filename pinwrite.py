import sys
import RPi.GPIO as GPIO

help = sys.argv

pin = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 35, 36, 37, 38, 40 ]

pinIn = help[2]
mode = help[1]

if int(mode) == 1:
	GPIO.setup(pin[int(pinIn)] , GPIO.OUT)
	GPIO.output(pin[int(pinIn)] , True)
	

if int(mode) == 0:
	GPIO.setup(pin[int(pinIn)] , GPIO.OUT)
	GPIO.output(pin[int(pinIn)] , False)
