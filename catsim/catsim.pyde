def setup():
    size(178,189)
    frameRate(12)


def draw():
    background('#FFFFFF')
    nyan = loadImage('dino.png')
    xpos = (frameCount % 4) * 192 * -1
    image(nyan, xpos,0)
