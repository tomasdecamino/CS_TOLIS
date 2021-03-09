# Tomás de Camino Beck
#CS TOLIS
#Shows how to create the Perseverance Parachute code
#https://time.com/5942177/perseverance-rover-parachute-message/

#Creates a constant array with base color '3'
#colors are coded as text categories
def constantArray(n):
    return ['3' for x in range(n)]

#decodes text color label to RGB color
def colorSwitch(c):
    switcher={'0':color(255,255,255),
              '1':color(255,0,0),
              '2':color(210,210,210),
              '3':color(255,0,0)}
    return switcher.get(c,color(0,0,0))

#Creates a circle sub-divided by d segments length s
#uses colorCode to fill with corresponding colors
def drawRingColor(s,d,rot,colorCode):
    step = TWO_PI/d
    for i in range(d):
        pushMatrix()
        translate(300,300)
        rotate(i*step+rot*step)
        fill(colorSwitch(colorCode[i]))
        arc(0, 0, s, s, 0, step, PIE)
        popMatrix()
        
#creates an array with the binary code of text
# '2' are separators
def textToColorB(t,n,p):
    colorCode = constantArray(n)
    templist = ['2','2','2']
    for character in t:
        templist.extend(bin(ord(character))[2:])
        templist.extend(['2','2','2'])
    colorCode[p:len(templist)+p]=templist
    return(colorCode)

#creates an array with the binary code of text
#replaces the first 1 of the binary letter code with 0
#as done in the perseverance code
def textToColor(t,n,p):
    colorCode = constantArray(n)
    templist = ['2','2','2']
    for character in t:
        templist.extend('0')
        templist.extend(bin(ord(character))[3:])
        templist.extend(['2','2','2'])
    colorCode[p:len(templist)+p]=templist
    return(colorCode)


def setup():
    size(600,600)
    ellipseMode(CENTER) 
    smooth(8)

def draw():
    background('#87CEEB')
    drawRingColor(500,80,0,textToColor("THINGS",80,0))
    drawRingColor(400,80,20,textToColor("MIGHTY",80,0))
    drawRingColor(200,80,-20,textToColor("DARE",80,0))
    fill(255)
    ellipse(300,300,50,50)
