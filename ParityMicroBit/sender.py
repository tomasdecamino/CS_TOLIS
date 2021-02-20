from microbit import *
import radio

radio.on()
 ##### Funtions. ######
def sendBits(m):
    for bit in message:
        if button_b.is_pressed():
            radio.send('1')
        else:
            radio.send(bit)
        sleep(200)
    
##### Main Code. ######

while True:
    # Button A sends  message.
    message = '101011'
    display.clear()
    if button_a.is_pressed():
        sendBits(message)
        display.scroll(message,delay=70)

     # Sends again if error is detected
    incoming = radio.receive()
    if incoming:
       display.show(Image.SAD)
       sendBits(message)


