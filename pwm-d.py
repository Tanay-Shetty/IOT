	
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

    duty_s=raw_input("Enter Brightness between (0 to 100):")

    duty=int(duty_s)

    pwm_led.ChangeDutyCycle(duty)

    time.sleep(0.2)
