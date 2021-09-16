#Tomas de Camino Beck
#Simple code to use with MicroBit

from microbit import *
from math import *

compass.calibrate()
#get initial heading in radians
directionBase = radians(compass.heading())

#get motor i2c address ussually 0x59
addr=i2c.scan()[-1]
i2c.init(freq=100000, sda=pin20, scl=pin19)

buf = bytearray(2)

#enable motors
buf[0]=0x70
buf[1]=1
i2c.write(89, buf)

def forward(speedL,speedR):
    #left
    buf[0]=0x21
    buf[1]=(100-speedL) * 127 // 100
    i2c.write(addr, buf)
    #right
    buf[0]=0x20
    buf[1]=(100-speedR) * 127 // 100
    i2c.write(addr, buf)

while True:
    direction = radians(compass.heading())

    
    diff = round((direction - directionBase) * 5)

    forward(20-diff,20+diff)
    
    sleep(500)
    forward(0,0)
    sleep(500)
