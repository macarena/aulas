class Cobra:
    corpo = []
    s = 10
    cor = color(0,255,0)
    dir = PVector(1,0)
    
    def __init__(self):
        x= 600 / 2 / self.s
        y= 600 / 2 / self.s
        
        for i in range(4):
            q = PVector(x - i, y)
            self.corpo.append(q)
            
    def desenha(self):
        self.anda()
        fill(self.cor)
        for qua in self.corpo:
            x = qua.x * self.s
            y = qua.y * self.s
            w = self.s
            h = self.s
            rect(x, y, w, h)
            
    def anda(self):
        q = self.corpo[0] + self.dir
        self.corpo.insert(0,q)
        del(self.corpo[-1])