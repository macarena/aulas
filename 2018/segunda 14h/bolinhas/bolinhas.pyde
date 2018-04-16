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

todas = []

def setup():
    size(800,600)
    for n in range(100):
        x = random(50, width-50)
        y = random(50, height-50)
        todas.append( bolinha(x, y) )
    
def draw():
    background(0)
    for b in todas:
        b.desenha()
        b.move()