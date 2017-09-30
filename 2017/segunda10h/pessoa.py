# coding: utf-8 #

nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))
comida = input('Que comida você gosta?')
lista = []

while comida:
    lista.append(comida)
    comida = input('Que comida você gosta?')

print ('Olá {}!'.format(nome))
print ('Se você tem {} anos, então você nasceu em {}'.format(idade, 2017-idade))
print ('Você gosta de:')

for item in lista:
    print (item)

if len(lista) > 3:
    print ('Quanta coisa! Cuidado pra não engordar...')
else:
    print ('Que delícia')
