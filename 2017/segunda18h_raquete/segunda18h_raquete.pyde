class raquete:
    x = 0
    y = 0
    w = 20
    h = 100
    p = False
    pontos = 0
    py = 80
    px = 30
    
    def __init__(self,player,b):
        self.b = b
        self.p = player
        if self.p:
            self.x = 10
            self.px = 120
        else:
            self.x = 770
            self.px = 600
    
    def desenha(self):
        self.move()
        self.placar()
        rect(self.x,self.y,self.w,self.h)
        b = self.b
        if b.y >= self.y and b.y <= self.y + self.h:
            if b.x >= self.x and b.x <= self.x + self.w:
                b.vx = b.vx * -1
        
    def move(self):
        if self.p:
            if mouseY > 0 and mouseY < height - self.h:
                self.y = mouseY
        else:
            if self.b.y > self.y + self.h/2:
                self.y += 2.5
            else:
                self.y -= 2.5
    
    def placar(self):
        text(self.pontos,self.px,self.py)
        if (not self.p and self.b.x < 0) or (self.p and self.b.x > 800):
            self.pontos += 1
            self.b.reset()
        
class bolinha:
    x = 400
    y = 300
    d = 15
    vx = -3
    vy = -3
    
    def desenha(self):
        self.move()
        ellipse(self.x,self.y,self.d,self.d)
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.y > height or self.y < 0:
            self.vy *= -1

    def reset(self):
        self.x = 400
        self.y = 300

b = bolinha()        
p1 = raquete(True,b)
p2 = raquete(False,b)

def setup():
    size(800,600)
    textSize(92)
    
def draw():
    background(0)
    p1.desenha()
    p2.desenha()
    b.desenha()