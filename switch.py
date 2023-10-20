	
import RPi.GPIO as GPIO

import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21,0)
while True:
    reading1=GPIO.input(16)
    reading2=GPIO.input(19)
    if(reading1==0 and reading2==0):
        GPIO.output(20,1)
        time.sleep(1)
        GPIO.output(20,0)
        time.sleep(1)
