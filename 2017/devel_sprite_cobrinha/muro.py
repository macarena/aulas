class Muro:
    cor = color(150,70,0)
    s = 10
    
    def __init__(self, w, h):
        self.estrutura = []
        cols = w/self.s
        lista = range(cols/3, 2*cols/3)
        for i in range(cols):
            if not i in lista:
                x = i * self.s
                y = 0
                self.estrutura.append(PVector(x,y))
                y = h - self.s
                self.estrutura.append(PVector(x,y))
        
        lins = h/self.s
        lista = range(lins/3, 2*lins/3)
        for i in range(lins):
            if not i in lista:
                y = i * self.s
                x = 0
                self.estrutura.append(PVector(x,y))
                x = w - self.s
                self.estrutura.append(PVector(x,y))
            
    def desenha(self):
        for tijolo in self.estrutura:
            fill(self.cor)
            rect(tijolo.x, tijolo.y, 10, 10)
        