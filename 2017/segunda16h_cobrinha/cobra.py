class Cobra:
    s = 10
    cor = color(0,255,0)
    corpo = []
    dirs = [PVector(1,0), PVector(-1,0), PVector(0,1), PVector(0,-1)]
    crescimento = 0
    tam = 4
    
    def __init__(self, comida, muro, w, h):
        self.comida = comida
        self.muro = muro
        self.tela = PVector(w,h) / self.s
        self.reset()
    
    def reset(self):
        self.comida.teletransporte()
        self.corpo = []
        q = self.tela / 2
        self.dir = self.dirs[int(random(4))]
        
        for i in range(self.tam):
            self.corpo.append(q-self.dir*i)
        
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
        reset = False
        for i in range(1,len(self.corpo)):
            if self.corpo[i] == self.corpo[0]:
                reset = True
                
        if reset:
            self.reset()
            
        # se ela bater no muro
        for tijolo in self.muro.estrutura:
            if tijolo == self.corpo[0] * self.s:
                self.reset()
        
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