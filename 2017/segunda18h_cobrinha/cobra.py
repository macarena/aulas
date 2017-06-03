class Cobra:
    corpo = []
    cor = color(0,255,0)
    dir = PVector(1,0)
    cresce = 0
    
    def __init__(self, tamanho, comida, w, h):
        self.s = tamanho
        self.comida = comida
        x= w / 2 / self.s
        y= h / 2 / self.s
        self.tela = PVector(w,h) / self.s
        
        for i in range(59):
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
        if self.cresce == 0:
            del(self.corpo[-1])
        else:
            self.cresce -= 1
        
        #se ela comeu a comida
        if self.corpo[0] * self.s == self.comida.pos:
            self.comida.mudaPos()
            self.cresce += self.comida.nutre
            
        #se bateu nela mesma
        for p in self.corpo[1:len(self.corpo)]:
            if self.corpo[0] == p:
                #fazer o gameover
                self.cor = color(100,200,150)
                
        #se sair da tela
        #pela direita
        if self.corpo[0].x >= self.tela.x:
            self.corpo[0].x = 0
        
        #pela esquerda
        if self.corpo[0].x < 0:
            self.corpo[0].x = self.tela.x

        #por baixo
        if self.corpo[0].y >= self.tela.y:
            self.corpo[0].y = 0
        
        #por cima
        if self.corpo[0].y < 0:
            self.corpo[0].y = self.tela.y
            
            
            
            
            