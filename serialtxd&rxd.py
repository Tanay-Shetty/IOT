import serial
import time
ser=serial.Serial(port='/dev/ttyUSB0',
                  baudrate=9600,
                  parity=serial.PARITY_NONE,
                  stopbits=serial.STOPBITS_ONE,
                  bytesize=serial.EIGHTBITS,
                  timeout=1)
counter=1
while True:
    ser.write(str(counter).encode())
    ser.write('.  SFN'.encode())
    p=ser.readline()
    print(p)
    counter+=1
    time.sleep()