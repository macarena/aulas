class bolinha:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.d = random(5, 50)
        self.cor = color(random(255),random(255),random(255))
        self.vx = random(-5, 5)
        self.vy = random(-5, 5)
    
    def desenha(self):
        fill(self.cor)
        ellipse(self.x, self.y, self.d, self.d)
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
        
        if self.y + self.d/2 > height or self.y - self.d/2 < 0:
            self.vy *= -1
        
        if self.x + self.d/2 > width or self.x - self.d/2 < 0:
            self.vx *= -1
            
    def rebate(self):
        self.vx *= -1
        self.vy *= -1

todas = []

def setup():
    size(800,600)
    x = random(50, width-50)
    y = random(50, height-50)
    todas.append( bolinha(x, y) )
    
def draw():
    background(0)
    for i in range(len(todas)):
        b = todas[i]
        b.desenha()
        b.move()
        for j in range(i+1,len(todas)):
            outra = todas[j]
            raios = b.d/2 + outra.d/2
            distancia = dist(b.x,b.y,outra.x,outra.y)
            if distancia < raios:
                b.rebate()
                outra.rebate()
        
def mouseClicked():
    todas.append( bolinha(mouseX, mouseY) )