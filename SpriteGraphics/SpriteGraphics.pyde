# Tomás de Camino Beck
# CS TOLIS
# UG: sprites, use of PGraphics, video game elements

posX = 195
posY = 145
speedX = 0
speedY = 0

def setup():
    size(300,300)
    frameRate(20)
    global sprite
    sprite = createGraphics(178, 189)
    global dino
    dino = loadImage('dino.png')

# evento to us arrow to move sprite
def keyPressed():
    global speedX, speedY
    if keyCode == UP:
        speedY = -3
    elif keyCode == DOWN:
        speedY = 3
    elif keyCode == LEFT:
        speedX = -3
    elif keyCode == RIGHT:
        speedX = 3

def draw():
    global posX, posY, speedX, speedY
    #movement of the sprite
    posX += speedX
    posY += speedY
    background(255)
    
    #it creates a canvas inside the main canvas
    sprite.beginDraw()
    sprite.background(255,0)
    #xpos changes the "frame" of the sprite
    #4 frames of size 192
    xpos = (frameCount % 4) * 192 * -1
    sprite.image(dino,xpos,0)
    sprite.endDraw()
    
    rect(100,100,100,100)
    #draws the sprite in posX, posY
    #s determines the display size of the sprite
    s = 0.3
    image(sprite,posX,posY, 178*s, 189*s)
