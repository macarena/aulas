class quadradinho:
    def __init__(self, coluna, linha):
        self.tamanho = 50
        self.x = self.tamanho * coluna
        self.y = self.tamanho * linha
        self.coluna = coluna
        self.linha = linha
        self.revelado = False
        self.bomba = False
        self.proximidade = 0
        
    def colocaBomba(self):
        self.bomba = True
        for linha in tabuleiro:
            for q in linha:
                if self.linha -1 <= q.linha <= self.linha +1:
                    if self.coluna -1 <= q.coluna <= self.coluna +1:
                        q.proximidade += 1
                
    def desenha(self):
        if self.revelado:
            if self.bomba:
                fill(255,0,0)
            else:
                fill(200)
        else:
            fill(255)
        rect(self.x, self.y, self.tamanho, self.tamanho)
        fill(0)
        textAlign(LEFT, TOP)
        textSize(42)
        text(self.proximidade, self.x, self.y)

tabuleiro = []

def setup():
    size(500,500)
    for linha in range(10):
        quadradinhos = [] 
        for coluna in range(10): 
            q = quadradinho(coluna,linha)  
            if int(random(0,2)) == 1:
                q.colocaBomba()
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