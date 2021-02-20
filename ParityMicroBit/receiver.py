# Tomás de Camino Beck
# Computer Science
# UG: Error correction, data trnasmission, parity check

from microbit import *
import radio

radio.on()
startTime = running_time()
message = ''
 ##### Funtions. ######

# counts '1'
def countBit(m):
    count = 0
    for bit in m:
        if bit == '1':
            count +=1
    return count

 # checks if string has an even number of '1'
 def parityCheck(m):
    if countBit(m)&1 == 0:
        return True
    else:
        return False
    

##### Main Code. ######

while True:
    # waits 10 seconds and resets.
    if (running_time()-startTime)>10000:
        message = ''
        display.clear()
        startTime = running_time()
     # Read any incoming message, and assables a string
    incoming = radio.receive()
    if incoming:
       message +=incoming
    
    #check if 6 bits received to display
    # change this is you send more from the sender
    if len(message)==6:
        if parityCheck(message):
            display.scroll(message,delay=70)
        else: #is parity not met, asks for the message again
            display.show(Image.SAD)
            radio.send('error')
            message = ''
            startTime = running_time()


