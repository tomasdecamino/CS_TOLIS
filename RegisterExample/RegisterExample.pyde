# Tomás de Camino Beck
# Computer Science with Python
# Register control emulation
# UG: using libraries and object, error handling, integer to binary, machine control
# UG: Some string manipulation

add_library('controlP5') #library for textfileds and buttons

def setup():
    size(600, 300)
    font = createFont("sansserif", 20)
    textSize(16)
    #Load backround image
    global img
    img = loadImage("8BitRegister.png")
    
    #creates the textfield object
    global inputBox
    inputBox = ControlP5(this)
    inputBox.addTextfield("input").setFocus(True).setSize(60, 20).setAutoClear(False).setPosition(92, 35)

def draw():
    background(0)
    image(img,0,0)
    fill(0)
    #error handling, if textfild is not an intenger
    try:
        number = int(inputBox.get(Textfield, "input").getText())
    except:
        number = 0
    #resturn the binary representation as string with "0" to the left to complete 8 characters
    binNumber=bin(number)[2:].rjust(8,"0")
    for i in range(8):
        text(binNumber[i], 112+i*52, 155)
