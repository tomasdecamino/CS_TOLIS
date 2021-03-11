# Add your Python code here. E.g.
from microbit import *

invader1 = Image(
             "09990:"
             "90909:"
             "09990:"
             "99099:"
             "90009")
             
invader2 = Image(
             "09990:"
             "90909:"
             "09990:"
             "09090:"
             "09090")

while True:
    display.show(invader1)
    sleep(500)
    display.show(invader2)
    sleep(500)
