# Tomás de Camino Beck
# CS TOLIS
# UG: Use of bitwise operations, error check, parity

def countBits(n,bits):
    count=0
    for i in range(bits):
        count+=(n&(1<<i)!=0)
    return(count)

def evenParity(n,bits):
    if(countBits(n,bits)&1):
      return n<<1|1
    else:
      return n<<1

def setup():
    size(300,300)
    textSize(20)


def draw():
    background(0)
    n = mouseX
    bs = bin(n)[2:]  
    text(bs,100,140)
    text(str(n)+" =",40,140)
    text(bin(evenParity(n,8))[2:],100,180)
    text(str(evenParity(n,8))+" =",40,180)
    
