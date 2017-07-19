esquerda = PVector(-1,0)
direita = PVector(1,0)
baixo = PVector(0,1)
cima = PVector(0,-1)

class Personagem:
    pos = PVector(0,0,0)
    dir = PVector(0,0,0)
    dirmove = {'C':False, 'B':False, 'D':False, 'E':False}
    s = 20
    
    def __init__(self):
        pass
        
    def update(self):
        self.pos += self.dir
        self.show()
        
    def show(self):
        fill(200,150,100)
        pushMatrix()
        translate(self.pos.x,self.pos.y,self.s/2)
        rotateZ(self.dir.heading())
        box(self.s)
        translate(0,0,self.s/2+1)
        fill(255,0,0)
        triangle(0,5,0,-5,7,0)
        popMatrix()
        
    def move(self, dir, move = True):
        if dir == cima:
            self.dirmove['C'] = move
        if dir == baixo:
            self.dirmove['B'] = move
        if dir == esquerda:
            self.dirmove['E'] = move
        if dir == direita:
            self.dirmove['D'] = move
            
        self.dir = PVector(0,0)
        for d in self.dirmove:
            if self.dirmove[d]:
                if d == 'C':
                    self.dir += cima
                if d == 'B':
                    self.dir += baixo
                if d == 'E':
                    self.dir += esquerda
                if d == 'D':
                    self.dir += direita

class Mapa:
    w = 200
    h = 200
    pos = PVector(0,0)
    
    def __init__(self):
        imagem = createImage(self.w,self.h, RGB)
        imagem.loadPixels()
        for i in range(len(imagem.pixels)):
            imagem.pixels[i] = color(random(255), 255, random(255))
        imagem.updatePixels()
        self.img = imagem
        
    def show(self):
        image(self.img, self.pos.x, self.pos.y)

p = Personagem()
m = Mapa()


def setup():
    size(500,500,P3D)

def draw():
    lights();
    background(0);
    
    camera(p.pos.x, p.pos.y + 100, p.pos.z + mouseY, #eyeX, eyeY, eyeZ
         p.pos.x,p.pos.y,p.pos.z, #centerX, centerY, centerZ
         0, 1, 0); #upX, upY, upZ
    m.show()
    p.update()



      
def keyPressed():
    dir = PVector(0,0)
    if keyCode == 37:
        dir = esquerda
    elif keyCode == 38:
        dir = cima
    elif keyCode == 39:
        dir = direita
    elif keyCode == 40:
        dir = baixo
    p.move(dir)

def keyReleased():
    dir = PVector(0,0)
    if keyCode == 37:
        dir = esquerda
    elif keyCode == 38:
        dir = cima
    elif keyCode == 39:
        dir = direita
    elif keyCode == 40:
        dir = baixo
    p.move(dir,False)