class Cobra():
    s = 10
    cor = color(0,255,0)
    corpo = []
    dir = PVector(1,0)
    
    def __init__(self):
        x = 10
        y = 40
        
        for i in range(10):
            self.corpo.append(PVector(x-i,y))
        
    def desenha(self):
        self.anda()
        for p in self.corpo:
            fill(self.cor)
            rect(p.x * self.s, p.y * self.s, self.s, self.s)
        
            
    def anda(self):
        novo = self.corpo[0] + self.dir
        self.corpo.insert(0,novo)
        del(self.corpo[-1])
            