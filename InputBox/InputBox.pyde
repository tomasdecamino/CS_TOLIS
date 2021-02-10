# Tomás de Camino Beck
# Computer Science with Python
# Usage of an input box
# UG: using libraries and objects, input boxes ans buttons

#library for textfileds and buttons
add_library('controlP5') 

def setup():
    size(600, 300)
    # changes text size
    textSize(36)
    
    #creates the object for buttons and textfields
    global inputBox
    inputBox = ControlP5(this)
    #creates a input box called "input" and changes some display parameters
    inputBox.addTextfield("input") \
      .setFocus(True) \
      .setSize(120, 20) \
      .setAutoClear(False) \
      .setPosition(92, 35)

    #Creates a button
    inputBox.addButton("clear") \
      .setPosition(215, 35) \
      .setSize(225, 20) \
      .getCaptionLabel() \
      .align(ControlP5.CENTER, ControlP5.CENTER)
    #determines wich function to call when the button is pressed
    inputBox.getController("clear").addListener(buttonPressed)

# This funtion established what the button will do
def buttonPressed(object):
    inputBox.get(Textfield, "input").clear()    


def draw():
    background(0)
    fill(255)
    # get the value from the text box and displays
    text(inputBox.get(Textfield, "input").getText(), 92, 155)
    
