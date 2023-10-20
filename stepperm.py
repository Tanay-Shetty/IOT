import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
pins=[17,18,22,23]
for i in pins:
    gpio.setup(i,gpio.OUT)
    gpio.output(i,0)
while True:
    data1=[1,0,1,0]
    for i in range(4):
        gpio.output(pins[i],data1[i])
    time.sleep(0.3)
    data2=[1,0,0,1]
    for i in range(4):
        gpio.output(pins[i],data2[i])
    time.sleep(0.3)
    data3=[0,1,0,1]
    for i in range(4): 
        gpio.output(pins[i],data3[i])
    time.sleep(0.3)
    data4=[0,1,1,0]
    for i in range(4):
        gpio.output(pins[i],data4[i])
    time.sleep(0.3)