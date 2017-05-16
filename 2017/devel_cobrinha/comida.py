class Comida:
    def __init__(self, escala):
        global width, height
        x = floor(random(width/10))
        y = floor(random(height/10))
        self.s = escala
        
        self.pos = PVector(x,y)
        
    def desenha(self):
        fill(255,0,0)
        rect(self.pos.x * self.s,self.pos.y * self.s,self.s,self.s)