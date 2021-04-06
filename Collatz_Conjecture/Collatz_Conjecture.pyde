# Tomás de Camino Beck
# Collatz number visualization

#collatz function
def collatz(n):
    if n % 2==0:
        return n/2
    else:
        return n*3 +1
    
#just to use degrees
def degree(rad):
    return rad * (PI/180)
    
def setup():
    size(600,400)
    background(0);
    for i in range(1,2000):
        sequence = []
        n = i
        #using while like a repeat until
        while True:
            sequence.insert(0,n)
            n = collatz(n)
            if n==1:
                sequence.insert(0,1) 
                break
        len = 7 #size of branches
        resetMatrix()
        translate(width/2,height)
        for s in sequence:
            rotate(degree(s)/150)
            strokeWeight(1);
            stroke(255, 10);
            line(0, 0, 0, -len);
            translate( 0, -len);
    
def draw():
    pass
