class Comida:
    cor = color(255,0,0)
    nutre = 2
    
    def __init__(self, tamanho, w, h):
        self.s = tamanho
        self.w = w
        self.h = h
        self.mudaPos()
        
    def mudaPos(self):
        x = int(random(0, self.w) / self.s)
        y = int(random(0, self.h) / self.s)
        self.pos = PVector(x,y) * self.s
        
    def desenha(self):
        fill(self.cor)
        rect(self.pos.x, self.pos.y, self.s, self.s)