from microbit import *
import radio

radio.on()
startTime = running_time()
message = ''
 ##### Funtions. ######

def countBit(m):
    count = 0
    for bit in m:
        if bit == '1':
            count +=1
    return count

def parityCheck(m):
    if countBit(m)&1 == 0:
        return True
    else:
        return False
    

##### Main Code. ######

while True:
    # Button A sends a "flash" message.
    if (running_time()-startTime)>10000:
        message = ''
        display.clear()
        startTime = running_time()
     # Read any incoming message.
    incoming = radio.receive()
    if incoming:
       message +=incoming
    
    #check if 6 bits received to display
    if len(message)==6:
        if parityCheck(message):
            display.scroll(message,delay=70)
        else:
            display.show(Image.SAD)
            radio.send('error')
            message = ''
            startTime = running_time()


