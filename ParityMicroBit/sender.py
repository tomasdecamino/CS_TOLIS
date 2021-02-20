# Tomás de Camino Beck
# Computer Science
# UG: Parity check, error correction, data transmission

from microbit import *
import radio

radio.on()
 ##### Funtions. ######

#count the number of ones in the string
def countBit(m):
    count = 0
    for bit in m:
        if bit == '1':
            count +=1
    return count

#makes number of ones even, add '0' or '1' at the end   
def parity(m): 
    if countBit(m)&1 == 0:
       return m + '0'
    else:
       return m + '1'


#sends each 'bit' one by one. If button b pressed adds error (a '1')
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
    # you can send any sequence of 1 and ceros (binary number)
    message = parity('10101') #adds parity bit at the end
    display.clear()
    # send message when button a pressed
    if button_a.is_pressed():
        sendBits(message)
        display.scroll(message,delay=70)

     # Receives a message if receiver detects error
     # then it sends the message again
    incoming = radio.receive()
    if incoming:
       display.show(Image.SAD)
       sendBits(message)


