from random import randint

class quadrado:
    revelado = False
    bomba = False
    vizinhos = 0
    s = 25
    marcado = False 
    
    def __init__(self, col, lin):
        self.col = col
        self.lin = lin
        self.x = col * self.s
        self.y = lin * self.s

    def desenha(self):
        if not self.revelado:
            fill(120,180,255)
            if self.marcado:
                image(flagimg, self.x, self.y, 25, 25)
                noFill()
            rect(self.x,self.y,self.s,self.s)
        else:
            fill(255)
            rect(self.x,self.y,self.s,self.s)
            if self.vizinhos > 0 : 
                fill(0)
                text(self.vizinhos,self.x+self.s/2,self.y+self.s - 5)
            if self.bomba:
                image(bombaimg, self.x, self.y, 25, 25)
                noFill()
                rect(self.x,self.y,self.s,self.s)
        
    def colocaBomba(self):
        if not self.bomba:
            self.bomba = True
            for q in self.meusVizinhos():
                q.vizinhos += 1
                    
    def revelar(self):
        global gameover
        if not self.revelado:
            self.revelado = True
            self.marcado = False
            if self.vizinhos == 0 and not self.bomba:
                for q in self.meusVizinhos():
                    q.revelar()
            if self.bomba:
                for q in tabuleiro:
                    if q.bomba:
                        q.revelar()
                gameover = True
                
    def marcar(self):
        qtm = sum(q.marcado for q in tabuleiro)
        if not self.revelado:
            if self.marcado:
                self.marcado = False
            elif qtm < qtb:
                self.marcado = True

    def meusVizinhos(self):
        viz = []
        for q in tabuleiro:
            if q.col >= self.col-1 and q.col <= self.col+1 and q.lin >= self.lin-1 and q.lin <= self.lin+1 and not (self.col == q.col and self.lin == q.lin):
                viz.append(q)
        return viz
            
linhas = 20
colunas = 30

tabuleiro = []
clicado = [-1,-1]
gameover = False
vitoria = False

qtb = 5

for lin in range(linhas):
    for col in range(colunas):
        tabuleiro.append(quadrado(col,lin))

while sum(q.bomba for q in tabuleiro) < qtb:
    aleatorio = randint(0,len(tabuleiro)-1)
    tabuleiro[aleatorio].colocaBomba()

def setup():
    global bombaimg, flagimg
    
    size(800,600)
    textAlign(CENTER)

    bombaimg = loadImage('bomba.jpg')
    flagimg = loadImage('flag.png')

def draw():
    background(255)
    textSize(16)
    corretas = 0
    for quadrado in tabuleiro:
        if clicado[0] == quadrado.col and clicado[1] == quadrado.lin:
            quadrado.revelar()
        quadrado.desenha()
    if gameover:
        textSize(120)
        fill(255,0,0)
        text("Game Over", width/2, height/2)
    if vitoria:
        textSize(120)
        fill(0,255,0)
        text("Parabéns", width/2, height/2)
    
def mouseClicked():
    global clicado
    col = int(mouseX / 25)
    lin = int(mouseY / 25)
    
    if not gameover:
        clicado = [col,lin]
        
def keyPressed():
    if key == ' ' and not gameover:
        col = int(mouseX / 25)
        lin = int(mouseY / 25)
        
        for q in tabuleiro:
            if col == q.col and lin == q.lin:
                q.marcar()