# Tomás de Camino Beck
# simple moving droplet with periodic boundaries
# try to balance the droplet
# UG: use of velocity, acceleration (no if statements)

from microbit import *
import math

posX = 2
posY = 2
vX = 0
vY =0

while True:
    display.clear()
    #gets acceleration as a value of {-1,0, 1}
    aX = round(accelerometer.get_x()/1024)
    aY = round(accelerometer.get_y()/1024)
    #set velocity in both directions
    vX+=aX
    vY+=aY
    #changes droplet position (uses modulo for periodic)
    posX=math.floor(posX + vX)%4
    posY=math.floor(posY + vY)%4
    #Display
    display.set_pixel(posX, posY, 9)
    sleep(800) #lower times for more sensitivity
    
