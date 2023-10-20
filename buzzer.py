import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(13,gpio.OUT)
def buzz(pitch,duration):
    period=1.0/pitch
    delay=period/2
    cycles=int(duration*pitch)
    for i in range(cycles):
        gpio.output(13,1)
        time.sleep(delay)
        gpio.output(13,0)
        time.sleep(delay)
pitch=1.0
duration=float(input("Enter duration in seconds:"))
buzz(pitch,duration)
