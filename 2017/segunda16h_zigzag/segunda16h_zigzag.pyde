from random import randint

class bolinha():
    v = 1
    d = 20
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def desenha(self):
        self.move()
        ellipse(self.x,self.y,self.d,self.d)
        
    def move(self):
        self.x += self.v

    def muda(self):
        self.v *= -1

class limite():
    def __init__(self, xe, xd, y):
        self.xe = xe
        self.xd = xd
        self.y = y
        
    def desenha(self):
        stroke(205,100,80)
        line(self.xe,self.y,self.xd,self.y)

class plataforma():
    limites = []
    
    def __init__(self,xe,xd):
        dir = -1
        tam = 0
        for n in range(600):
            self.limites.append(limite(xe,xd, n))
            xe += dir
            xd += dir
            tam -= 1
            
            if tam <= 0:
                tam = randint(50,150)
                dir *= -1
            
    def desenha(self):
        for l in self.limites:
            l.y += 1
            l.desenha()

b = bolinha(400,500)
p = plataforma(350,450)

def setup():
    size(800,600)
    
def draw():
    background(255)
    p.desenha()
    b.desenha()
    
def mousePressed():
    b.muda()