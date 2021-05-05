import random
import RPi.GPIO as GPIO
import time
import os

ledMode = (random.randint(1,4))  
print (ledMode)

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)



while True:
 if GPIO.input(27) ==GPIO.HIGH:


    if ledMode == 1:
        GPIO.output(26,1)
        time.sleep(0.3)
        GPIO.output(12,1)
        time.sleep(0.3)
        GPIO.output(13,1)
        time.sleep(0.3)  
        GPIO.output(6,1)
        time.sleep(0.3)
        GPIO.output(5,1)
        time.sleep(0.3)
        GPIO.output(25,1)
        time.sleep(0.3)
        GPIO.output(24,1)
        time.sleep(0.3)
        GPIO.output(23,1)
        time.sleep(0.3)  
        GPIO.output(22,1)
        time.sleep(0.3)    
        GPIO.output(4,1)
        time.sleep(0.3)

    elif ledMode == 2:

        GPIO.output(26,1)
        GPIO.output(4,1)
        time.sleep(0.3)

        GPIO.output(12,1)
        GPIO.output(22,1)
        time.sleep(0.3)
        

        GPIO.output(13,1)
        GPIO.output(23,1)
        time.sleep(0.3)  

        GPIO.output(6,1)
        GPIO.output(24,1)
        time.sleep(0.3)

        GPIO.output(5,1)
        GPIO.output(25,1)
        time.sleep(0.3)

    elif ledMode == 3:

        GPIO.output(26,1)
        GPIO.output(4,1)
        time.sleep(0.3)

        GPIO.output(26,0)
        GPIO.output(4,0)
        

        GPIO.output(12,1)
        GPIO.output(22,1)
        time.sleep(0.3)

        GPIO.output(12,0)
        GPIO.output(22,0)
        
        GPIO.output(13,1)
        GPIO.output(23,1)
        time.sleep(0.3) 

        GPIO.output(13,0)
        GPIO.output(23,0)

        GPIO.output(6,1)
        GPIO.output(24,1)
        time.sleep(0.3)

        GPIO.output(6,0)
        GPIO.output(24,0)

        GPIO.output(5,1)
        GPIO.output(25,1)
        time.sleep(0.3)

        GPIO.output(5,0)
        GPIO.output(25,0)

    else :

        for x in range(0,15): 
            pin = randint (4,22,23,24,25,5,6,13,12,26)
            GPIO.output(pin,1)
            time.sleep(0.3)
            GPIO.output(pin,0)
            x += 1
            print (pin)


        
     




