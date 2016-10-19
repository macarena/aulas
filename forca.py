import random

lista= ['FUTEBOL', 'JOGADOR', 'INSTAGRAM', 'BANANA', 'YOUTUBE', 'COCIELO', 'CRISTIAN', 'ABACAXI']

i = random.randint(0, len(lista)- 1)

palavra_secreta = 'ABACAXI'
#apagar a linha abaixo
print palavra_secreta

palavra_exibida = '-'*len(palavra_secreta)
print palavra_exibida
erros = 0
#comeca o loop do jogo
while( erros <7 and palavra_secreta != palavra_exibida):
    letra = raw_input('Digite uma letra: ')
    letra = letra.upper()
    tem_letra = 'nao'
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra:
            tem_letra = 'sim'
            palavra_exibida =  '{0}{1}{2}'.format(palavra_exibida[:i], letra, palavra_exibida[i + 1:])
    if tem_letra == 'nao':
        erros = erros + 1
    #else:

    print erros
    print palavra_exibida
