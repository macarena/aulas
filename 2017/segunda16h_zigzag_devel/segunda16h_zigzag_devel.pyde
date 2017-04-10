from random import randint

margem = 50

class bolinha():
    v = 1
    d = 15
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def desenha(self):
        self.move()
        fill(100)
        translate(self.x,self.y,self.d)
        sphere(self.d)
        translate(-self.x,-self.y,-self.d)
        
    def move(self):
        self.x += self.v

    def muda(self):
        self.v *= -1

class parte():
    
    def __init__(self, dir, tamanho, pos):
        self.dir = dir
        self.tamanho = tamanho
        self.pos = pos
        
    def desenha(self):
        global margem
        m = margem
        p = self
        
        if self.dir > 0:
            beginShape(QUAD_STRIP)
            vertex(-m,0,-m)
            vertex(-m + p.tamanho,0 - p.tamanho,-m)
            
            vertex(-m,0,0)
            vertex(-m + p.tamanho,0 - p.tamanho,0)
            
            vertex(m,0,0)
            vertex(m + p.tamanho,0 - p.tamanho,0)
            
            vertex(m,0,-m)
            vertex(m + p.tamanho,0 - p.tamanho,-m)
            
            endShape()
            translate(p.tamanho,-p.tamanho)
        else:
            beginShape(QUAD_STRIP)
            vertex(-m,0,-m)
            vertex(-m - p.tamanho,0 - p.tamanho,-m)
            
            vertex(-m,0,0)
            vertex(-m - p.tamanho,0 - p.tamanho,0)
            
            vertex(m,0,0)
            vertex(m - p.tamanho,0 - p.tamanho,0)
            
            vertex(m,0,-m)
            vertex(m - p.tamanho,0 - p.tamanho,-m)
            
            endShape()
            translate(-p.tamanho,-p.tamanho)        

class plataforma():
    global margem
    
    def __init__(self):
        self.xe = -margem
        self.xd = margem
        self.dir = 1 # esquerda = -1 / direita = +1
        self.caminho = [parte(1,50,0)]
        self.passo = 0
        self.pos = 0
        
    def addParte(self):
        ultimo = self.caminho[-1]
        dir = ultimo.dir * -1
        tamanho = randint(50,300)
        pos = ultimo.pos + ultimo.tamanho
        self.caminho.append(parte(dir,tamanho, pos))
        
    def desenha(self):
        m = margem

        self.atualiza()
        fill(0,100,255)
        translate(0,self.pos,0)
        for p in self.caminho:
            p.desenha()
        
    def atualiza(self):
        self.xe += self.dir
        self.xd += self.dir
        self.pos += 1
        atual = self.caminho[self.passo]
        if self.pos > atual.pos + atual.tamanho :
            self.passo += 1
            self.dir *= -1
        if sum(p.tamanho for p in self.caminho) - self.pos < 1000:
            self.addParte()

b = bolinha(0,0)
p = plataforma()

def setup():
    size(800,600,P3D)
    noStroke()
    
def draw():
    translate(width/2,height-100,0)
    rotateX(PI/3)
    ortho()
    lights()
    background(255)
    b.desenha()
    p.desenha()
    
def mousePressed():
    b.muda()