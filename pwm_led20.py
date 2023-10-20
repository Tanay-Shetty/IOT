import RPi.GPIO as GPIO
import time
led_pin=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
pwm_led=GPIO.PWM(led_pin,500)
pwm_led.start(100)
while True:
    for i in range(100):
        pwm_led.ChangeDutyCycle(i)
        time.sleep(0.2)
        
    for i in range(100):
        pwm_led.ChangeDutyCycle(100-i)
        time.sleep(0.2)