class Comida:
    pos = PVector(0,0)
    cor = color(255,0,0)
    s = 10
    
    def __init__(self,muro, w,h):
        self.w = w
        self.h = h
        self.m = muro
        self.teletransporte()
        
    def teletransporte(self):
        x = int(random(0,self.w) / self.s)
        y = int(random(0,self.h) / self.s)
        self.pos = PVector(x,y) * self.s
        
        for tijolo in self.m.estrutura:
            if tijolo == self.pos:
                self.teletransporte()
        
    def desenha(self):
        fill(self.cor)
        rect(self.pos.x, self.pos.y, self.s, self.s)