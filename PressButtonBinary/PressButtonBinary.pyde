# Tomas de Camino Beck
#CS course with Pyhton

# Simple press button code

# button list
# list is organized [x,y,size, True/False]
buttons = [
           [50,100,100,True],
           [150,100,100, False],
           [250,100,100, False],
           [350,100,100, False]
           ]


pressButton = False

def setup():
    size(800, 300)
    textSize(50)

def draw():
    background(0)
    stroke(200)
        
    global buttons

    # draw buttons
    dec = 0
    for i, button in enumerate(buttons):
        if button[3]:
            fill(255)
            dec+=((2**(len(buttons)-1-i))*button[3])
        else:
            fill(0)
        rect(button[0], button[1], button[2], button[2])
        #calculate denary number (reversed)

    
    #display text
    #change colors based on decimal number
    fill(map(dec,0,15,0,255),100,255-map(dec,0,15,0,255))
    text("=",500 ,165)
    text(dec,600 ,165)


# event that is triggered when mouse button pressed
def mousePressed():
    pressButtons()


# check if mouse is over a button
def pressButtons():
    global buttons
    for button in buttons:
        if (button[0]< mouseX < (button[0]+button[2]) and button[1]< mouseY < (button[1]+button[2])):
            button[3] = not button[3]
            
    
