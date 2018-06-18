class quadradinho:

    def __init__(self, coluna, linha):
        self.tamanho = 50
        self.x = self.tamanho * coluna
        self.y = self.tamanho * linha
        self.coluna = coluna
        self.linha = linha
        self.revelado = False
        self.marcado = False
        self.bomba = False
        self.proximidade = 0
        
    def colocaBomba(self):
        self.bomba = True
        for q in self.vizinhos():
            q.proximidade += 1
        
    def vizinhos(self):
        lista = []
        for linha in tabuleiro:
            for q in linha:
                if self.linha - 1 <= q.linha <= self.linha + 1:
                    if self.coluna - 1 <= q.coluna <= self.coluna + 1:
                        if self.coluna != q.coluna or self.linha != q.linha:
                            lista.append(q)
        return lista
                
    def clicado(self):
        if not self.revelado and not self.marcado:
            self.revelado = True
            if self.bomba:
                global gameover
                gameover = True
            
            elif self.proximidade == 0:
                for q in self.vizinhos():
                    q.clicado()
    
    def marcar(self):
        if not self.revelado and contaMarcados() < qt_bombas or self.marcado:
            self.marcado = not self.marcado
            if contaMarcados() == qt_bombas:
                verificarVitoria()
        
    def desenha(self):
        if self.revelado:
            if self.bomba:
                fill(255, 0, 0)
            else:
                fill(200)
        else:
            if self.marcado:
                fill(0,0,255)
            else:
                fill(255)
        rect(self.x, self.y, self.tamanho, self.tamanho)
        
        if not self.bomba and self.revelado and self.proximidade > 0:
            fill(0)
            textSize(self.tamanho)
            x = self.x + self.tamanho / 2
            y = self.y + self.tamanho / 2
            text(self.proximidade, x, y)

def contaBombas():
    total = 0
    for linha in tabuleiro:
        for quadradinho in linha:
            if quadradinho.bomba:
                total += 1
    return total

def contaMarcados():
    total = 0
    for linha in tabuleiro:
        for quadradinho in linha:
            if quadradinho.marcado:
                total += 1
    return total

def verificarVitoria():
    for linha in tabuleiro:
        for q in linha:
            if q.bomba and not q.marcado:
                return
    global vitora
    vitoria = True

tabuleiro = []
qt_bombas = 10
gameover = False
vitoria = False

def setup():
    size(500, 550)
    textAlign(CENTER, CENTER)
    for linha in range(10):
        quadradinhos = []
        for coluna in range(10):
            q = quadradinho(coluna, linha)
            quadradinhos.append(q)
        tabuleiro.append(quadradinhos)
        
    while contaBombas() < qt_bombas:
        l = int(random(0, 9))
        c = int(random(0, 9))
        q = tabuleiro[l][c]
        if not q.bomba:
            print(l,c)
            q.colocaBomba()
        
def draw():
    background(0)
    textSize(24)
    fill(255)
    text("Bombas: " + str(qt_bombas), width/4, 525)
    text("Marcados: " + str(contaMarcados()), width*3/4, 525)
    
    for linha in tabuleiro:
        for q in linha:
            q.desenha()
            
    if gameover:
        telaGameOver()
        
    if vitoria:
        telaVitoria()

def mousePressed():
    coluna, linha = pegaPosicao()
    q = tabuleiro[linha][coluna]
    if not gameover:
        q.clicado()
        
def keyPressed():
    if keyCode == 32:
        coluna, linha = pegaPosicao()
        q = tabuleiro[linha][coluna]
        if not gameover:
            q.marcar()
        
def telaGameOver():
    fill(0, 0, 0, 180)
    rect(0, 0, width, height)
    fill(255)
    textSize(72)
    text("GAME OVER",width/2,height/2)
    
def telaVitoria():
    fill(0, 0, 0, 180)
    rect(0, 0, width, height)
    fill(255)
    textSize(72)
    text("PARABÉNS",width/2,height/2)

def pegaPosicao():
    coluna = int(mouseX / 50)
    linha = int(mouseY / 50)
    return coluna, linha