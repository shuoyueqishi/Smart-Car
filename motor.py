import time
import RPi.GPIO as GPIO

class Motor:
    def __init__(self):
        self.pwmaPin=3
        self.pwmbPin=5
        self.ain1Pin=7
        self.ain2Pin=11
        self.bin1Pin=13
        self.bin2Pin=15
        self.stbyPin=19
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)  
        #self.pwma-pin3
        GPIO.setup(self.pwmaPin,GPIO.OUT) 
        self.pwma=GPIO.PWM(self.pwmaPin,1000)
        self.pwma.start(0)
        #self.pwmb-pin5 
        GPIO.setup(self.pwmbPin,GPIO.OUT)
        self.pwmb=GPIO.PWM(self.pwmbPin,1000)
        self.pwmb.start(0)
        #AIN1-pin7
        GPIO.setup(self.ain1Pin,GPIO.OUT)
        #AIN2-pin11
        GPIO.setup(self.ain2Pin,GPIO.OUT)
        #BIN1-pin13
        GPIO.setup(self.bin1Pin,GPIO.OUT)
        #BIN2-pin15
        GPIO.setup(self.bin2Pin,GPIO.OUT)
        #STBY-pin19
        GPIO.setup(self.stbyPin,GPIO.OUT)
        #left wheel forward rotates

    def leftFront(self):
        GPIO.output(self.ain1Pin,GPIO.HIGH)
        GPIO.output(self.ain2Pin,GPIO.LOW)
        self.pwma.ChangeDutyCycle(20)

    #left wheel backward ratates
    def leftBack(self):
        GPIO.output(self.ain1Pin,GPIO.LOW)
        GPIO.output(self.ain2Pin,GPIO.HIGH)
        self.pwma.ChangeDutyCycle(20)

    #right wheel forward rotate
    def rightFront(self):
        GPIO.output(self.bin1Pin,GPIO.LOW)
        GPIO.output(self.bin2Pin,GPIO.HIGH)
        self.pwmb.ChangeDutyCycle(20)

    #right wheel backward rotates
    def rightBack(self):
        GPIO.output(self.bin1Pin,GPIO.HIGH)
        GPIO.output(self.bin2Pin,GPIO.LOW)
        self.pwmb.ChangeDutyCycle(20)

    #vehicle moves forward
    def forward(self):
        self.leftFront()
        self.rightFront()
        GPIO.output(self.stbyPin,GPIO.HIGH)

    #vehicle moves backward
    def backward(self):
        self.leftBack()
        self.rightBack()
        GPIO.output(self.stbyPin,GPIO.HIGH)

    #vehicle turns left 
    def turnLeft(self):
        self.leftBack()
        self.rightFront()
        GPIO.output(self.stbyPin,GPIO.HIGH)

    #vehicle turn right
    def turnRight(self):
        self.leftFront()
        self.rightBack()
        GPIO.output(self.stbyPin,GPIO.HIGH)

    #brake
    def Braking(self):
        GPIO.output(7,GPIO.LOW)
        GPIO.output(11,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(self.stbyPin,GPIO.HIGH)

    
