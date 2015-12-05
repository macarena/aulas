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
  def __init__(self):
      pass
  def sair(self):
      pass
  def ajuda(self): 
      pass
  def status(self):
      pass
  def cansado(self):
      pass
  def descansar(self):
      pass
  def explorar(self):
      pass
  def fugir(self):
      pass
  def ataque(self):
      pass
  def ataque_inimigo(self):
      pass
 
Comandos = {
  'sair': Jogador.sair,
  'ajuda': Jogador.ajuda,
  'status': Jogador.status,
  'descansar': Jogador.descansar,
  'explorar': Jogador.explorar,
  'fugir': Jogador.fugir,
  'atacar': Jogador.ataque,
  }