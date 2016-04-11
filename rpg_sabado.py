# coding=utf8
from random import randint
 
class Personagem:
  def __init__(self):
    self.nome = ""
    self.hp = 1
    self.hp_max = 1
  def dano(self, inimigo):
    dano = min(max(randint(0, self.hp) - randint(0, inimigo.hp), 0),inimigo.hp)
    inimigo.hp = inimigo.hp - dano
    if dano == 0:
        print "%s esquivou do ataque de %s." % (inimigo.nome, self.nome)
    else: print "%s feriu %s!" % (self.nome, inimigo.nome)
    return inimigo.hp <= 0
 
class Monstro(Personagem):
  def __init__(self, jogador):
    Personagem.__init__(self)
    self.nome = 'Goblin'
    self.hp = randint(1, jogador.hp)
 
class Jogador(Personagem):
  def __init__(self, nome):
      Personagem.__init__(self)
      self.estado = 'normal'
      self.hp = 10
      self.hp_max = 10
      self.nome = nome
  def sair(self):
      print "Nada acontece."
  def ajuda(self): 
      print "Nada acontece."
  def status(self):
      print "Nada acontece."
  def cansado(self):
      print "Nada acontece."
  def descansar(self):
      print "Nada acontece."
  def explorar(self):
      print "Nada acontece."
  def fugir(self):
      print "Nada acontece."
  def ataque(self):
      print "Nada acontece."
  def ataque_inimigo(self):
      print "Nada acontece."
 
Comandos = {
      'sair': Jogador.sair,
      'ajuda': Jogador.ajuda,
      'status': Jogador.status,
      'descansar': Jogador.descansar,
      'explorar': Jogador.explorar,
      'fugir': Jogador.fugir,
      'atacar': Jogador.ataque,
}
  
pergunta = raw_input("Qual o nome do seu personagem? ")
p = Jogador(pergunta)
print "(digite ajuda para obter uma lista de comandos)"
print "%s entra em uma caverna escura, procurando por aventura." % p.nome

while p.hp > 0:
    linha = raw_input("> ")
    args = linha.split()
    if len(args) > 0:
        comandoEncontrado = False
        for c in Comandos.keys():
            if args[0] == c[:len(args[0])]:
                Comandos[c](p)
                comandoEncontrado = True
                break
        if not comandoEncontrado:
            print "%s não entende esse comando." % p.nome