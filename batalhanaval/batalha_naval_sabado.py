from random import randint

class Navio:
    pass

    def __init__(self, nome):
        self.nome = nome
        self.linha = randint(0, linhas -1)
        self.coluna = randint(0, colunas -1)

tabuleiro = []

colunas = 10
linhas = 10

for x in range(linhas):
    tabuleiro.append(["O"] * colunas)


def print_tabuleiro(t):
    for linha in t:
        print " ".join(linha)

navios = [Navio("titanic"),Navio("bote"),Navio("caravela")]

print "Vamos jogar batalha naval! UHUUUUU!!!"

final = False
tentativas = 0

print_tabuleiro(tabuleiro)

while final == False:
    print "Você chutou %s vezes" % tentativas
    tentativas += 1

    chute_linha = input("qual linha?") -1
    chute_coluna = input("qual coluna?") -1

    if chute_linha == navio_linha and chute_coluna == navio_coluna:
        print "PARABÉNS! Acertou mizeravi..."
        final = True

    else:
        print "Você errou"
        '''
        if chute_linha < 0 or chute_coluna < 0 or chute_linha > linhas -1 or chute_coluna > colunas -1:
            print "Você chutou fora do tabuleiro"
        else:
            tabuleiro[chute_linha][chute_coluna] = "X"
        '''


    print_tabuleiro(tabuleiro)
