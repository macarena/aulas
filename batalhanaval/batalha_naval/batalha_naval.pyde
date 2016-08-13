from random import randint
from time import sleep

class Desenho:
    quadrado = 50
    cor = 255
    cor2 = [255, 0 ,0]

class Vazio(Desenho):
    pass
    
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        self.oculto = True
        self.x = linha * self.quadrado
        self.y = coluna * self.quadrado
    
    def desenha(self):
        if self.oculto:
            fill(self.cor)
        else:
            fill(self.cor2)
        rect(self.x,self.y,self.quadrado,self.quadrado,4)
        print "desenhando vazio em %s|%s ->  %s|%s" % (self.linha, self.coluna,self.x, self.y)

class Navio(Desenho):
    pass

    def __init__(self, nome, tamanho = 1):
        self.nome = nome
        self.vivo = True
        self.tamanho = tamanho

    def posiciona(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        self.x = linha * self.quadrado
        self.y = coluna * self.quadrado
        
    def desenha(self):
        if self.vivo:
            fill(self.cor)
        else:
            fill(self.cor2)
        rect(self.x,self.y,self.quadrado,self.quadrado,50)
        print "desenhando navio em %s|%s ->  %s|%s" % (self.linha, self.coluna,self.x, self.y)

class Tabuleiro:
    tentativas = 0

    def __init__(self, navios, linhas, colunas):
        if colunas:
            self.colunas = colunas
        else:
            self.colunas = linhas
        self.linhas = linhas
        self.casas = []

        for x in range(self.linhas):
            linha = []
            for y in range(self.colunas):
                linha.append(Vazio(x,y))    
            self.casas.append(linha)

        for navio in navios:
            self.arrumar(navio)

    def imprime(self):
        for y, linha in enumerate(self.casas):
            for x, casa in enumerate(linha):
                casa.desenha()
                
        print tabuleiro.casas

    def arrumar(self,navio):
        casa = ''
        while not isinstance(casa,Vazio):
            linha = randint(0, self.linhas -1)
            coluna = randint(0, self.colunas -1)
            casa = self.casas[linha][coluna]
        
        print "colocando navio em %s|%s" % (linha,coluna)
        self.casas[linha][coluna] = navio
        navio.posiciona(linha, coluna)

    def chute(self,linha,coluna):
        print "\nVocê chutou %s vezes\n" % self.tentativas

        if self.fora(linha,coluna):
            print "\nVocê chutou fora do tabuleiro\n"
            return

        if self.repetido(linha,coluna):
            print "\nVocê já tentou aí\n"
            return

        self.tentativas += 1

        print "Tiro disparado..."
        sleep(2)
        

        if isinstance(self.casas[linha][coluna], Navio):
            print "\nPARABÉNS! Acertou mizeravi...\n"
            self.casas[linha][coluna].vivo = False
        else:
            print "\nVocê errou!\n"
            self.casas[linha][coluna] = "X"

        sleep(2)

    def fora(self,x,y):
        if x < 0 or x > self.linhas:
            return True
        if y < 0 or y > self.colunas:
            return True
        return False

    def repetido(self,x,y):
        if self.casas[x][y] == "X":
            return True
        if isinstance(self.casas[x][y],Navio) and self.casas[x][y].vivo == False:
            return True
        return False

def vivos(navios):
    vivos = [n for n in navios if n.vivo]
    if len(vivos) > 0:
        return True
    else:
        return False

navios = [Navio("titanic"), Navio("bote"), Navio("caravela")]
tabuleiro = Tabuleiro(navios,5,3)

#print "\nVamos jogar batalha naval! UHUUUUU!!!\n"


'''
while vivos(navios):
    #chute_linha = input("qual linha?") -1
    #chute_coluna = input("qual coluna?") -1

    #tabuleiro.chute(chute_linha,chute_coluna)
    tabuleiro.chute(randint(0,2),randint(0,2))

    tabuleiro.imprime()
'''
#print "\n\n\nParabéns!!\n\nVocê conseguiu em %s tentativas" % tabuleiro.tentativas






def setup():
    size(500, 550)
    tabuleiro.imprime()
    
def draw():
    pass