import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # set board mode to Broadcom
GPIO.setup(18, GPIO.OUT)  # set up pin 18
 
while True:
    GPIO.output(18, 1)  # turn on pin 18
    print 'led on'
    time.sleep(1) #delay for 1 seconds
    GPIO.output(18,0)  #turn off pin 18
    print 'led is off'
    time.sleep(2)
