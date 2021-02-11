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
    print(str(reading)+","+ bA+","+ bB)
