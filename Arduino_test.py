#This file is used for testing arduino commands dose not affect the core program
import serial
import time

arduino=serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)

#print("Enter 1 to turn ON LED and 0 to turn OFF LED")

def fwd():
    arduino.write(b'f')
    #print("fwd")

def back():
    arduino.write(b'f')
    #print("back")

def left():
    arduino.write(b'f')
    #print("left")

def right():
    arduino.write(b'f')
    #print("right")

def Stop():
    arduino.write(b'c')
    #print("stop")
while 1:
    
    datafromUser=input()

    if datafromUser == '1':
        fwd()

        print("LED  turned ON")
    elif datafromUser == '0':
        Stop()
        print("LED turned OFF")