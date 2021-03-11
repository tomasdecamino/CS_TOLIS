#Tomás de Camino Beck
#Clinometer
# UG: Use of images, accelerometer, if statements and functions


from microbit import *
import math

angle = 0

# converts reading to  -90 to 90 angles
# uses https://www.hobbytronics.co.uk/accelerometer-info
def toAngle(aX,aY,aZ):
    temp = aY/math.sqrt((aX*aX)+(aZ*aZ))
    angle = math.atan(temp)*(180/math.pi)
    return angle

line = Image("00900:"
             "00900:"
             "00900:"
             "00900:"
             "00900")

while True:
    # reads the angle
    if button_a.is_pressed():
        ax = (accelerometer.get_x()-32)
        ay = (accelerometer.get_y()-0)
        az = (accelerometer.get_z()-32)
        display.scroll("%.1f" % toAngle(ax,ay,az),delay=150)
    
    #displays last angle measurement
    if button_b.is_pressed():
        display.scroll("%.1f" % toAngle(ax,ay,az),delay=150)
    display.clear()
    display.show(line)