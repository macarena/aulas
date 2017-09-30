nome  = input('Qual seu nome?')
print('Prazer em conhece-lo(a), {}'.format(nome))

numero = 9
tentativas = 0
conta = 0
while conta*conta != numero:
    conta = input("Você sabe a raiz quadrada de {}?".format(numero))
    conta = int(conta)
    tentativas += 1

print('Parabéns, {}! Você acertou em {} tentativas.'.format(nome, tentativas))