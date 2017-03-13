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
            rect(self.col*self.s,self.lin*self.s,self.s,self.s)
            
linhas = 20
colunas = 30

tabuleiro = []

for col in range(colunas):
    for lin in range(linhas):
        tabuleiro.append(quadrado(col,lin))

def setup():
    size(800,600)

def draw():
    background(255)
    for quadrado in tabuleiro:
        quadrado.desenha()
    