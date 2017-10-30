from random import randint

nome = input('Qual é o seu nome?')
print('Prazer em conhece-lo(a),{}'.format(nome))
print('Pensei em um numero entre 1 e 100. tente asivinhar qual é.')

numero = randint(0, 100)
tentativas = 0
resposta = 0
while resposta != numero:
    resposta = input('Digite seu palpite e tecle enter')
    resposta = int(resposta)
    tentativas += 1
    if numero > resposta:
        dif = 'maior'
    if numero < resposta:
        dif = 'menor'
    if numero == resposta:
        dif = 'IGUAL'
    print('O numero que eu pensei é {} que esse'.format(dif))

print('Parabéns, {}! Você acertou em {} tentativas.'.format(nome, tentativas))