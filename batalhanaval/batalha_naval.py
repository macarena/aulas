#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
from time import sleep

class Navio:
    pass

    def __init__(self, nome, tamanho = 1):
        self.nome = nome
        self.vivo = True
        self.tamanho = tamanho

    def posiciona(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    def __repr__(self):
        if self.vivo:
            return "O"
        else:
            return "!"

class Tabuleiro:
    tentativas = 0

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

    def imprime(self):
        for linha in self.casas:
            print " ".join(str(casa) for casa in linha)

    def arrumar(self,navio):
        casa = '_'
        while casa != "O":
            linha = randint(0, self.linhas -1)
            coluna = randint(0, self.colunas -1)
            casa = self.casas[linha][coluna]
        
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
tabuleiro = Tabuleiro(navios,3,3)

print "\nVamos jogar batalha naval! UHUUUUU!!!\n"

tabuleiro.imprime()

while vivos(navios):
    chute_linha = input("qual linha?") -1
    chute_coluna = input("qual coluna?") -1

    tabuleiro.chute(chute_linha,chute_coluna)

    tabuleiro.imprime()

print "\n\n\nParabéns!!\n\nVocê conseguiu em %s tentativas" % tabuleiro.tentativas