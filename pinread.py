import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

help = sys.argv

pin = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40 ]

channel = int(help[1])

GPIO.setup(pin[channel], GPIO.IN)
	
if GPIO.input(pin[channel]):
	print "1"
else:
	print "0"

