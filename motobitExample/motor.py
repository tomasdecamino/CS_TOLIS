from microbit import *
from motobit import *

while True:
    if button_a.is_pressed():
        Motor.enable()
        motor_left.set_speed(100)
        motor_right.set_speed(100)
        sleep(1000)
        motor_left.set_speed(100, Motor.REVERSE)
        motor_right.set_speed(100)
        sleep(200)
        motor_left.set_speed(100)
        motor_right.set_speed(100)