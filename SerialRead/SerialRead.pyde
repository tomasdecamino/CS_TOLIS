# Tomas de Camino Beck
# simple example to connect Micro:Bit using serial to Processing
# At the en d micro:Bit code

add_library('serial') 

inString = "0"

def setup():
    size(800,300)
    println(Serial.list())
    #Choose proper serial device from list
    myPort = Serial(this,Serial.list()[5], 115200)
    myPort.bufferUntil(10)

def serialEvent(port):
    global inString
    inString = port.readString()
    
def draw():
    background(0)
    #nothing yet
    ellipse(400+int(inString),150,100,100)
    text(inString,10,10)
    
"""
# Micro:Bit Simple code sending accelerometer data to Processing

from microbit import *

while True:
    reading = accelerometer.get_x()
    if reading > 20:
        display.show("R")
    elif reading < -20:
        display.show("L")
    else:
        display.show("-")
    print(reading)
"""    
