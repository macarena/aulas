from random import randint
from time import sleep

class Navio:
    pass

    def __init__(self, nome):
        self.nome = nome
        self.vivo = True

    def posiciona(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    def __repr__(self):
        if self.vivo:
            return "W"
        else:
            return "!"

class Tabuleiro:
    tentativa = 0

    def __init__(self, navios, linhas, colunas):
        if colunas:
            self.colunas = colunas
        else:
            self.colunas = linhas
        self.linhas = linhas
        self.casas = []
        for x in range(linhas):
            self.casas.append(["O"] * colunas)
        for navio in navios:
            self.arrumar(navio)

    def arrumar(self, navio):
        casa = ''
        while casa != "O":
            linha = randint(0, self.linhas -1)
            coluna = randint(0, self.colunas -1)
            casa = self.casas[linha][coluna]
        
        self.casas[linha][coluna] = navio
        navio.posiciona(linha,coluna)

    def mostra(self):
        for linha in self.casas:
            print " ".join(str(casa) for casa in linha)

    def chute(self, linha, coluna):
        if isinstance(self.casas[linha][coluna], Navio):
            print "\nParabéns! Acertou mizerávi...\n"
            self.casas[linha][coluna].vivo = False
        else:
            print "\nVocê errou!\n"
            self.casas[linha][coluna] = "X"

barcos = [Navio("titanic"),Navio("bote"),Navio("caravela")]

print "Vamos jogar batalha naval! UHUUUUU!!!"

final = False

tabuleiro = Tabuleiro(barcos, 5, 5)

tabuleiro.mostra()

while True:
    chute_linha = input("qual linha?") -1
    chute_coluna = input("qual coluna?") -1

    tabuleiro.chute(chute_linha,chute_coluna)

    tabuleiro.mostra()
