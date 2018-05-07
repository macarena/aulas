class quadradinho:
    def __init__(self, coluna, linha):
        self.tamanho = 50
        self.x = self.tamanho * coluna
        self.y = self.tamanho * linha
        self.revelado = False
        self.bomba = False
    
    def desenha(self):
        if self.revelado:
            if self.bomba:
                fill(255,0,0)
            else:
                fill(200)
        else:
            fill(255)
        rect(self.x, self.y, self.tamanho, self.tamanho)

tabuleiro = []

def setup():
    size(500,500)
    for linha in range(10):
        quadradinhos = [] 
        for coluna in range(10): 
            q = quadradinho(coluna,linha)  
            if int(random(0,2)) == 1:
                q.bomba = True
            quadradinhos.append(q)
        tabuleiro.append(quadradinhos)
        
def draw():
    for linha in tabuleiro:
        for q in linha:
            q.desenha()

def mousePressed():
    coluna = int(mouseX / 50)
    linha = int(mouseY / 50)
    q = tabuleiro[linha][coluna]
    q.revelado = True