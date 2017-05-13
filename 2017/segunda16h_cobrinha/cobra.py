class pCorpo():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cobra():
    s = 10
    cor = color(0,255,0)
    
    def __init__(self):
        self.corpo = [pCorpo(10,40)]
        self.corpo.append(pCorpo(10 -1, 40 ))
        self.corpo.append(pCorpo(10 -2, 40 ))
        self.corpo.append(pCorpo(10 -3, 40 ))
        
    def desenha(self):
        self.anda()
        for p in self.corpo:
            fill(self.cor)
            rect(p.x * self.s, p.y * self.s, self.s, self.s)
        
            
    def anda(self):
        x = self.corpo[0].x + 1
        y = self.corpo[0].y
        self.corpo.insert(0,pCorpo(x,y))
        del(self.corpo[-1])
            
