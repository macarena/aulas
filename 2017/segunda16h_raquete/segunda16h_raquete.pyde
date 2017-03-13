class raquete:
    x = 0
    y = 0
    h = 80
    w = 20
    vel = 3.8
    player = False
    pontos = 0

    def __init__(self, player, bolinha):
        self.b = bolinha
        if player:
            self.x = 10
            self.player = True;
            self.px = 50
        else:
            self.x = 800 - 10 - self.w
            self.px = 700
            
    def desenha(self):
        self.move()
        self.bateu()
        self.placar()
        rect(self.x,self.y,self.w,self.h)
        
    def move(self):
        if self.player:
            self.y = mouseY
        else:
            if self.y > self.b.y - self.h/2:
                self.y -= self.vel
            else:
                self.y += self.vel   
            
    def bateu(self):
        if self.b.x > self.x and self.b.x < self.x + self.w + self.b.d/2:
             if self.b.y > self.y and self.b.y < self.y + self.h:
                 self.b.vx *= -1
                 
    def placar(self):
        text(self.pontos, self.px, 150)
        if (self.player and self.b.x > 800) or (not self.player and self.b.x < 0):
            self.b.reset()
            self.pontos += 1

class bola:
    x = 400
    y = 300
    d = 20
    vx = -4
    vy = -4
    
    def desenha(self):
        self.move()
        ellipse(self.x,self.y,self.d,self.d)
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.y > 600 - self.d/2 or self.y < self.d/2:
            self.vy *= -1
          
    def reset(self):
        self.x = 400
        self.y = 300

b = bola()
p1 = raquete(True,b)
p2 = raquete(False,b)


def setup():
    size(800,600)
    textSize(96)
    
def draw():
    background(0)
    p1.desenha()
    p2.desenha()
    b.desenha()