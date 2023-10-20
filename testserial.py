import RPi.GPIO as GPIO
import serial
import time
ser=serial.Serial('/dev/serial0',9600)
ser.write('HI HOW R U STUDENT ')
while True:
	print(ser.read())

