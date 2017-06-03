class Cobra:
    s = 10
    cor = color(0,255,0)
    corpo = []
    dir = PVector(1,0)
    crescimento = 0
    
    def __init__(self, comida, w, h):
        self.comida = comida
        self.tela = PVector(w,h) / self.s
        x = 10
        y = 40
        
        for i in range(4):
            self.corpo.append(PVector(x-i,y))
        
    def desenha(self):
        self.anda()
        for p in self.corpo:
            fill(self.cor)
            rect(p.x * self.s, p.y * self.s, self.s, self.s)
        
            
    def anda(self):
        novo = self.corpo[0] + self.dir
        self.corpo.insert(0,novo)
        if self.crescimento == 0 :
            del(self.corpo[-1])
        else:
            self.crescimento -= 1
        
        #se ela pegar a comida
        if self.corpo[0] * self.s == self.comida.pos:
            self.comida.teletransporte()
            self.crescimento = 2
            
        #se ela bater no proprio corpo
        for i in range(1,len(self.corpo)):
            if self.corpo[i] == self.corpo[0]:
                #aqui sera o gameover
                self.cor = color(255,0,255)
        
        #se ela sair da tela
        #pela direita
        if self.corpo[0].x >= self.tela.x:
            self.corpo[0].x = 0
        
        #pela esquerda
        if self.corpo[0].x < 0:
            self.corpo[0].x = self.tela.x -1
        
        #por cima
        if self.corpo[0].y < 0:
            self.corpo[0].y = self.tela.y -1
        
        #por baixo
        if self.corpo[0].y >= self.tela.y:
            self.corpo[0].y = 0