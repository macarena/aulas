from random import randint
palavras=[
    'bola',
    'carro',
    'poste',
    'arvore',
    'mochila',
    'compurtador',
    'lego',
    'eletricista',
    'tomada',
    'tomate'
]

vidas= 8
n = randint(0, len(palavras)-1)
palavra = palavras[n]
print(palavra)
tracinhos=[]
for l in palavra:
    tracinhos.append('_')
chutes = []

while vidas > 0 and  '_' in tracinhos:
    print(" ".join(tracinhos))
    print ('você tem mais {} tentativas'.format(vidas))
    chute = input('Que letra você acha que tem na palavra? ')
    if chute in chutes:
        print('você ja chutou essa letra')
        continue
    chutes.append(chute)
    erros =  True
    for i in range(len(palavra)):
        if chute == palavra[i]:
            erros = False
            tracinhos[i] = chute

    if erros:
        vidas-=1
        
if vidas == 0:
    print ( 'GAME OVER!!!')
else:
    print ('PARABENS VOCÊ ACERTOU!!!')