"""

Projeto para visualização de listas bi-dimensionals
Lúdico: Imagine um robo que cospe um monte de robozinhos,
e cada um desses robozinhos cospe um monte de moedinhas

"""

class moeda:
    def __init__(self, coluna, linha):
        self.tamanho = 50
        self.x = self.tamanho * coluna
        self.y = self.tamanho * linha
        
    def desenha(self):
        fill(255,255,0)
        ellipseMode(CORNER)
        ellipse(self.x, self.y, self.tamanho, self.tamanho)

robo = []

def setup():
    size(500,500)
    for linha in range(10):
        robozinho = []
        for coluna in range(10):
            robozinho.append(moeda(coluna, linha))
        robo.append(robozinho)

def draw():
    for robozinho in robo:
        for moeda in robozinho:
            moeda.desenha()