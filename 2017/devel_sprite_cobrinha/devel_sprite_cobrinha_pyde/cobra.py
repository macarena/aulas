class Cobra:
    corpo = []
    cor = color(0,255,0)
    dir = PVector(1,0)
    cresce = 0
    
    def __init__(self, tamanho, comida, muro, w, h):
        self.s = tamanho
        self.comida = comida
        self.muro = muro.estrutura
        x= w / 2 / self.s
        y= h / 2 / self.s
        self.tela = PVector(w,h) / self.s
        self.head = loadImage("head.png")
        self.body = loadImage("body.png")
        self.tail = loadImage("tail.png")
        self.turn = loadImage("turn.png")
        
        for i in range(8):
            q = PVector(x - i, y)
            self.corpo.append(q)
            
    def desenha(self):
        self.anda()
        for i in range(len(self.corpo)):
            qua = self.corpo[i]
            x = qua.x * self.s + self.s/2
            y = qua.y * self.s + self.s/2
            imageMode(CENTER)
            pushMatrix()
            translate(x,y)
            
            if i == 0:
                img = self.head
                angulo = PVector.angleBetween(PVector(0,-1),self.dir)
                if self.dir == PVector(-1,0):
                    angulo *= -1
                rotate(angulo)
            elif i == len(self.corpo) - 1:
                img = self.tail
                dif = self.corpo[i-1] - qua
                angulo = PVector.angleBetween(PVector(0,-1),dif)
                if dif == PVector(-1,0):
                    angulo *= -1
                rotate(angulo)
            else:
                dif1 = self.corpo[i-1] - qua
                dif2 = self.corpo[i+1] - qua
                angulo = PVector.angleBetween(dif1,dif2)
                if degrees(angulo) == 90:
                    angulo = PVector.angleBetween(PVector(0,-1),dif1)
                    #rotate(angulo)
                    img = self.turn
                else:
                    img = self.body
            

            
            image(img,0,0,self.s,self.s)
            popMatrix()
            
    def anda(self):
        q = self.corpo[0] + self.dir
        self.corpo.insert(0,q)
        if self.cresce == 0:
            del(self.corpo[-1])
        else:
            self.cresce -= 1
        
        #se sair da tela
        #pela direita
        if self.corpo[0].x >= self.tela.x:
            self.corpo[0].x = 0
        
        #pela esquerda
        if self.corpo[0].x < 0:
            self.corpo[0].x = self.tela.x -1

        #por baixo
        if self.corpo[0].y >= self.tela.y:
            self.corpo[0].y = 0
        
        #por cima
        if self.corpo[0].y < 0:
            self.corpo[0].y = self.tela.y -1
            
        #se ela comeu a comida
        if self.corpo[0] * self.s == self.comida.pos:
            self.comida.mudaPos()
            self.cresce += self.comida.nutre
            
        #se bateu nela mesma
        for p in self.corpo[1:len(self.corpo)]:
            if self.corpo[0] == p:
                #fazer o gameover
                self.cor = color(100,200,150)
        
        #se ela bateu no muro
        for tijolo in self.muro:
            if self.corpo[0] == tijolo:
                #fazer o gameover
                self.cor = color(100,200,150)