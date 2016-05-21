from random import randint

tabuleiro = []

colunas = 5
linhas = 5

for x in range(linhas):
    tabuleiro.append(["O"] * colunas)


def print_tabuleiro(t):
    for linha in t:
        print " ".join(linha)

navio_linha = randint(0, linhas -1)
navio_coluna = randint(0, colunas -1)

print "Vamos jogar batalha naval! UHUUUUU!!!"

final = False
tentativas = 0

while final == False:
    print "Você chutou %s vezes" % tentativas
    tentativas +1

    chute_linha = input("qual linha?")
    chute_coluna = input("qual coluna?")

    if chute_linha == navio_linha and chute_coluna == navio_coluna:
        print "PARABÉNS! Acertou mizeravi..."
        final = True

    else:
        print "Você errou"

    print_tabuleiro(tabuleiro)
