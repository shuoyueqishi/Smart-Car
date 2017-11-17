import RPi.GPIO as GPIO
import time

class Ultrasonic:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        self.trig_pin=21
        self.echo_pin=23
        GPIO.setup(self.trig_pin,GPIO.OUT)
        GPIO.setup(self.echo_pin,GPIO.IN)

    def getDistance(self):
        GPIO.output(self.trig_pin,False)
        time.sleep(0.2)
        GPIO.output(self.trig_pin,True)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin,False)
        while GPIO.input(self.echo_pin)==0:
            t_start=time.time()

        while GPIO.input(self.echo_pin)==1:
            t_end=time.time()

        t=t_end-t_start
        distance=t*17150#unit of distance is cm
        distance=round(distance,3)
        return distance
