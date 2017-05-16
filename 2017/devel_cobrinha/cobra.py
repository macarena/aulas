class Cobra:
    corpo = []
    cor = color(0,255,0)
    dir = PVector(1,0)
    
    def __init__(self,escala):
        global width, height
        self.s = escala
        x= 600 / 2 / self.s
        y= 600 / 2 / self.s
        
        for i in range(4):
            q = PVector(x - i, y)
            self.corpo.append(q)
            
    def desenha(self,comida):
        self.anda(comida)
        fill(self.cor)
        for qua in self.corpo:
            x = qua.x * self.s
            y = qua.y * self.s
            w = self.s
            h = self.s
            rect(x, y, w, h)
            
    def anda(self,comida):
        #adicionando mais um quadrado a frente
        x = self.corpo[0].x
        y = self.corpo[0].y
        q = PVector(x,y) + self.dir
        self.corpo.insert(0, q)
        
        #removendo ultimo quadrado
        if not self.comendo(comida):
            del(self.corpo[-1])
        
    def comendo(self,comida):
        print(self.corpo[0])
        print(comida.pos)
        if self.corpo[0] == comida.pos:
            return True
        else:
            return False