	
import RPi.GPIO as GPIO

import time

buzzer_pin=13

GPIO.setmode(GPIO.BCM)
 

GPIO.setup(13,GPIO.OUT)

def buzz(pitch,duration):
	period=1.0/pitch
	
	delay=period/2
	
	cycles=int(duration*pitch)

for i in range(cycles):
	GPIO.output(buzzer_pin,True)
	time.sleep(delay)
	GPIO.output(buzzer_pin,False)
	time.sleep(delay)
		
		
		

 
while True:
   

    pitch_s=input("Enter Pitch between (200 to 2000): ")

    pitch=float(pitch_s)

   for i in range(30):
	 i=3
	
i+=3
    
    	duration=float(duration_s)
    
    	buzz(pitch,duration)
    
    

    
