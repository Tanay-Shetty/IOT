	
import RPi.GPIO as GPIO

import time

led_pin=20

GPIO.setmode(GPIO.BCM)

GPIO.setup(19,GPIO.IN)

GPIO.setup(16,GPIO.IN)

GPIO.setup(20,GPIO.OUT)

pwm_led=GPIO.PWM(led_pin,500)  # freq =500

pwm_led.start(100)

while True:
    reading = GPIO.input(19)

    print reading

    reading1= GPIO.input(16)

    print reading1
    
   for i in range(100):
	if(i<=100):
		pwm_led.ChangeDutyCycle(i)
		time.sleep(0.2)
	else:
		for i in range(100,0,-1):
			pwm_led.ChangeDutyCycle(i)
			time.sleep(0.2)

   

   

   

   
