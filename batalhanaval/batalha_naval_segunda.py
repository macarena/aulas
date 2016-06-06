from random import randint

print "Vamos jogar batalha naval"

jogo = True

tabuleiro = []

linhas = 5
colunas = 5

for x in range(linhas):
    tabuleiro.append(["O"] * colunas)

navio_linha = randint(0,linhas-1)
navio_coluna = randint(0,colunas-1)

def mostra_tabuleiro(t):
    for l in t:
        print " ".join(l)

while jogo:
    mostra_tabuleiro(tabuleiro)

    chute_linha = input("qual linha?") -1
    chute_coluna = input("qual coluna?") -1

    if chute_linha == navio_linha and chute_coluna == navio_coluna:
        print "Parabéns! Você acertou!!"
        jogo = False
    elif chute_linha >= linhas or chute_coluna >= colunas:
        print "Você chutou fora do tabuleiro"
    elif tabuleiro[chute_linha][chute_coluna] == "X":
        print "Você já chutou aí"
    else:
        tabuleiro[chute_linha][chute_coluna] = "X"
