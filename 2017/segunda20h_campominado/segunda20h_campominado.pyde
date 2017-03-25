from random import randint

class quadrado:
    revelado = False
    bomba = False
    vizinhos = 0
    s = 25
    
    def __init__(self, col, lin):
        self.col = col
        self.lin = lin

    def desenha(self):
        if not self.revelado:
            fill(255)
            rect(self.col*self.s,self.lin*self.s,self.s,self.s)
        else:
            fill(0,0,255)
            rect(self.col*self.s,self.lin*self.s,self.s,self.s)
        if self.bomba:
            fill(255,0,0)
            rect(self.col*self.s,self.lin*self.s,self.s,self.s)
        
            
linhas = 20
colunas = 30

tabuleiro = []
clicado = [-1,-1]

qtb = 40

for col in range(colunas):
    for lin in range(linhas):
        tabuleiro.append(quadrado(col,lin))

for n in range(qtb):
    aleatorio = randint(0,len(tabuleiro))
    tabuleiro[aleatorio].bomba = True

def setup():
    size(800,600)

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