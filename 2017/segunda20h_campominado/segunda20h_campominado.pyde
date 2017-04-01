from random import randint

class quadrado:
    revelado = False
    bomba = False
    vizinhos = 0
    s = 25
    
    def __init__(self, col, lin):
        self.col = col
        self.lin = lin
        self.x = col * self.s
        self.y = lin * self.s

    def desenha(self):
        if not self.revelado:
            fill(120,180,255)
            rect(self.x,self.y,self.s,self.s)
        else:
            fill(255)
            rect(self.x,self.y,self.s,self.s)
            fill(0)
            text(self.vizinhos,self.x+self.s/2,self.y+self.s - 5)
        if self.bomba:
            fill(255,0,0)
            rect(self.x,self.y,self.s,self.s)
        
    def colocaBomba(self):
        if not self.bomba:
            self.bomba = True
            for q in tabuleiro:
                if q.col >= self.col-1 and q.col <= self.col+1 and q.lin >= self.lin-1 and q.lin <= self.lin+1 and not (self.col == q.col and self.lin == q.lin):
                    q.vizinho += 1
            
linhas = 20
colunas = 30

tabuleiro = []
clicado = [-1,-1]

qtb = 100

for col in range(colunas):
    for lin in range(linhas):
        tabuleiro.append(quadrado(col,lin))

while sum(q.bomba for q in tabuleiro) < qtb:
    aleatorio = randint(0,len(tabuleiro)-1)
    #tabuleiro[aleatorio].bomba = True
    tabuleiro[aleatorio].colocaBomba()

def setup():
    size(800,600)
    textAlign(CENTER)
    textSize(16)

def draw():
    background(255)

    for quadrado in tabuleiro:
        if clicado[0] == quadrado.col and clicado[1] == quadrado.lin:
            quadrado.revelado = True
        quadrado.desenha()
    
def mouseClicked():
    global clicado
    col = int(mouseX / 25)
    lin = int(mouseY / 25)
    
    clicado = [col,lin]