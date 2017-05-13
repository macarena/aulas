from random import randint

class bolinha():
    v = 1
    d = 20
    le = 0
    ld = 800
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def novoLimite(self, limite):
        self.le = limite.xe
        self.ld = limite.xd
        
    def desenha(self):
        self.move()
        ellipse(self.x,self.y,self.d,self.d)
        
    def move(self):
        self.x += self.v
        if self.x < self.le or self.x > self.ld:
            print 'bolinha morreu'

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
    limites = [ limite(350,450,0) ]
    dir = 1
    tam = 0
    
    def addLimite(self):
        u = self.limites[-1]
        xe = u.xe + self.dir
        xd = u.xd + self.dir
        self.limites.append(limite(xe,xd, 0))
        self.tam -= 1
            
        if self.tam <= 0:
            self.tam = randint(50,150)
            self.dir *= -1
            
        if len(self.limites) > 600:
            del self.limites[0]
    
    
    '''
    Antigo método construtor
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
    '''
            
            
    def desenha(self):
        self.addLimite()
        for l in self.limites:
            l.y += 1
            if l.y == b.y:
                b.novoLimite(l)
            l.desenha()

p = plataforma()
b = bolinha(400,500)

def setup():
    size(800,600)
    
def draw():
    print(len(p.limites))
    background(255)
    p.desenha()
    b.desenha()
    stroke(0)
    line(b.le, b.y-10, b.le, b.y+10)
    line(b.ld, b.y-10, b.ld, b.y+10)
    
def mousePressed():
    b.muda()