#coding: utf-8
from random import randint

def imprime_lista(lista):
    for i in range(len(lista)):
        print(lista[i])

jogadores = ["Neymar", "Messi", "Ronaldo", "Maradona", "Pelé", "Zico", "Cristiano Ronaldo", "Rivaldo"]

print("Esses são os jogadores do meu time:")
imprime_lista(jogadores)

print("Ainda faltam três... Quem você sugere?")
while len(jogadores) < 11:
    jogador = input("Digite um nome de jogador: ")
    jogadores.append(jogador)

print("Agora o time está completo:")
imprime_lista(jogadores)

numero = randint(0,len(jogadores)-1)
aleatorio = jogadores[numero]

print("Soletrando nome do jogador: " + aleatorio)

for letra in aleatorio:
    print(letra)