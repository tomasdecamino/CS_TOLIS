#Tomas de Camino Beck
#Curso processing python
#Sierpinsky Triangle
# Understanding Goal: recursivity, reference system (processing)
# trigonometry, geometry


def setup():
    size(600,600)
    smooth(8)
    stroke(255,5)
    background(0)
    
def draw():
    background(0)
    noFill()
    stroke(mouseX,600-mouseX,mouseY,80)
    # call recursive function
    sierpinskyTriangle(300,50,550,5)


#Recursive function that creates sierpinski with "iter" iterations
def sierpinskyTriangle(x,y,l,iter):    
    if iter>0:
        pushMatrix() #set coordinate system
        translate(x,y) #translate 0,0
        triangle(0,0,l/2,sin(PI/3)*l,-l/2,sin(PI/3)*l) # draw triangle
        sierpinskyTriangle(0,0,l/2,iter-1) # call itself
        pushMatrix() #set new coordinate system
        translate(0,sin(PI/3)*l)
        sierpinskyTriangle(l/4,-sin(PI/3)*l/2,l/2,iter-1)
        sierpinskyTriangle(-l/4,-sin(PI/3)*l/2,l/2,iter-1)
        triangle(0,0,l/4,-sin(PI/3)*l/2,-l/4,-sin(PI/3)*l/2)
        popMatrix() #return to previous coordinate system
        popMatrix() #return to previous coordinate system
