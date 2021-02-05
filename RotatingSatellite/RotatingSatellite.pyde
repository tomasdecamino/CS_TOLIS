#Tomas de Camino Beck
#CS course with Pyhton

a = PI # a is a global variable

def setup():
    size(500,500)
    ellipseMode(CENTER)
    

def draw():
    background(0)
    noFill()
    stroke(255,70)
    global a #note that we have to tell python that 'a' is global
    n = 5
    for i in range(n):
      pushMatrix()
      translate(250,250)
      rotate(2*PI*i/n)
      satellite(-60,0,300,a,color(255, 204, 0))
      satellite(60,0,300,a+PI,color(205, 104, 200))
      popMatrix()
      
    a+=0.02 #iterator to change angles


    
def satellite(x,y,d,rot,c):
    pushMatrix()
    translate(x,y)
    noFill()
    strokeWeight(2)
    stroke(255,80)
    ellipse(0,0,d,d)
    fill(255)
    strokeWeight(20)
    stroke(c,200)
    point(cos(rot)*d/2,sin(rot)*d/2)
    popMatrix()
    

    
