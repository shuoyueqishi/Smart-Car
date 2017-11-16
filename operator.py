from motor import Motor
from getch import _GetchUnix
import time
import sys
import termios
import tty
var='a'
getch=_GetchUnix()
motor=Motor()
while var!='q':
    print('q-quit,f-forward,b-backward,l-turnLeft,r-turnRight')
    var=getch()
    if var=='f':
        motor.forward()
        print('Move forward')
    if var=='b':
        motor.backward()
        print('Move backward')
    if var=='l':
        motor.turnLeft()
        print('Turn left')
    if var=='r':
        motor.turnRight()
        print('Turn right')

