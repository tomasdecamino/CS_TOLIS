# Add your Python code here. E.g.
from microbit import * 
# Servo control: 
# 50 = ~1 millisecond pulse all right 
# 75 = ~1.5 millisecond pulse center 
# 100 = ~2.0 millisecond pulse all left 
pin15.set_analog_period(20)

while True: 
	pin15.write_analog(75)
	sleep(1000)
	pin15.write_analog(20)
	sleep(1000)
	pin15.write_analog(100)
	sleep(10000)
