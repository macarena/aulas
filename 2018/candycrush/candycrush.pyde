from random import randint

class Pedrinha:
    def __init__(self):
        possibilidades = [
            {'cor': color(255,0,0), 'forma': 'quadrado'},
            {'cor': color(255,255,0), 'forma': 'triangulo'},
            {'cor': color(0,255,0), 'forma': 'circulo'},
            {'cor': color(0,0,255), 'forma': 'losango'}
        ]
        sorteio = randint(0, len(possibilidades) - 1)
        self.cor = possibilidades[sorteio]['cor']
        self.forma = possibilidades[sorteio]['forma']
        
    def desenha(self, x, y, w, h):
        fill(self.cor)
        if self.forma == 'circulo':
            ellipseMode(CENTER)
            ellipse(x+w/2, y+h/2, w * 0.8, h * 0.8)
        elif self.forma == 'quadrado':
            rectMode(CENTER)
            rect(x+w/2, y+h/2, w * 0.8, h * 0.8)
        elif self.forma == 'triangulo':
            x1 = x + w * 0.2
            x2 = x + w * 0.5 
            x3 = x + w * 0.8 
            y1 = y + h * 0.8 
            y2 = y + h * 0.2
            y3 = y + h * 0.8 
            triangle(x1,y1,x2,y2,x3,y3)
        elif self.forma == 'losango':
            pushMatrix()
            translate(x+w/2, y+h/2)
            rotate(PI/4)
            rectMode(CENTER)
            rect(0,0,w*0.6,h*0.6)
            popMatrix()

class Casinha:
    def __init__(self, coluna, linha, altura, largura):
        self.coluna = coluna
        self.linha = linha
        self.altura = altura
        self.largura = largura
        self.x = self.coluna * self.largura
        self.y = self.linha * self.altura
        self.conteudo = None
        
    def recebePedrinha(self, pedrinha):
        if self.conteudo == None:
            self.conteudo = pedrinha
        
    def desenha(self):
        fill(120,0,30)
        rectMode(CORNER)
        rect(self.x, self.y, self.largura, self.altura)
        if self.conteudo != None:
            self.conteudo.desenha(self.x, self.y, self.largura, self.altura)

class Tabuleiro:
    def __init__(self):
        self.linhas = 20
        self.colunas = 20
        self.casinhas = []
        for coluna in range(self.colunas):
            lista = []
            for linha in range(self.linhas):
                lista.append(Casinha(coluna,linha, height/self.linhas, width/self.colunas))
            self.casinhas.append(lista)
            
    def listaCasinhas(self):
        todas = []
        for lista in self.casinhas:
            for casinha in lista:
                todas.append(casinha)
        return todas
        
    def desenha(self):
        for casinha in self.listaCasinhas():
            casinha.desenha()

def setup():
    global t
    
    size(600,600)
    t = Tabuleiro()

    for casinha in t.listaCasinhas():
        casinha.recebePedrinha(Pedrinha())
    
def draw():
    t.desenha()
    
def mouseClicked():
    coluna = mouseX / width / t.colunas