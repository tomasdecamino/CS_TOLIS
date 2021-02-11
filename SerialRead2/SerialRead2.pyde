# Tomas de Camino Beck
# simple example to connect Micro:Bit using serial to Processing
# At the end micro:Bit code
# takes finormation from accelerometer X and two buttons

add_library('serial') 

inString = "0,false,false"

def setup():
    size(800,300)
    println(Serial.list())
    #Choose proper serial device from list
    myPort = Serial(this,Serial.list()[5], 115200)
    myPort.bufferUntil(10) #finds new line
    frameRate(20)

def serialEvent(port):
    global inString
    # sometimes the string comes with trailing newline symbols
    # so they are removed
    inString = port.readString().replace("\n", "").replace("\r", "")
    
def draw():
    background(0)
    #nothing yet
    data = inString.split(",")
    print(data)
    if(data[1]=="True"):
        fill(255,0,0)
    if(data[2]=="True"):
        fill(0,255,0)
    ellipse(400+int(data[0]),150,100,100)
    fill(255)
    text(data[0],10,10)
    
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
    bA = str(button_a.is_pressed())
    bB = str(button_b.is_pressed())
    # Prepares a comma separated string
    print(str(reading)+","+ bA+","+ bB+",")
"""    
