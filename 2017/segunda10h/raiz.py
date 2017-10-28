from random import randint

nome  = input('Qual seu nome?')
print('Prazer em conhece-lo(a), {}'.format(nome))

numero = randint(1,10)
tentativas = 0
conta = 0
while conta != numero:
    conta = input("Você sabe a raiz quadrada de {}?".format(numero*numero))
    conta = int(conta)
    tentativas += 1

print('Parabéns, {}! Você acertou em {} tentativas.'.format(nome, tentativas))