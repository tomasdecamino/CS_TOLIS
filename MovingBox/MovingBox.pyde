# Tomas de Camino Beck
# CS TOlIS
# UG: program dinamical objects and interaction, simulation physics

posX = 195
posY = 145
speedX = 0
speedY = 0

def keyPressed():
    global speedX, speedY
    
    if keyCode == UP:
        speedX = 0
        speedY = -4

    elif keyCode == DOWN:
        speedX = 0
        speedY = 4

    elif keyCode == LEFT:
        speedX = -4
        speedY = 0

    elif keyCode == RIGHT:
        speedX = 4
        speedY = 0
        
def setup():
    size(400,300)
    frameRate(30)
    background(0)
    noStroke()
    #ernest = createFont('Ernest.ttf', 30)
    #textFont(ernest)
    textAlign(CENTER)


def draw():
    global posX, posY, speedX, speedY
    posX += speedX
    posY += speedY

    fill(0,80)
    rect(0,0, width,height)

    fill('#FFFFFF')
    rect(posX, posY, 10, 10)
