import time
import serial
ser=serial.Serial('/dev/serial1',9600)
while True:
	ser.write('HI STUDENTS I AM GOOD')
	p=ser.read()
	print(p)
	print('\n')
	ser.write(p)
	time.sleep(0.1)
