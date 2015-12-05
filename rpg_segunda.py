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
    Personagem.__init__(self)
    self.estado = 'normal'
    self.hp = 10
    self.hp_max = 10
  def sair(self):
    print "%s Não pode achar uma saída e morre de fome.\nR.I.P." % self.nome
    self.hp = 0
  def ajuda(self): print Comandos.keys()
  def status(self): print "Saúde de %s: %d/%d" % (self.nome, self.hp, self.hp_max)
  def cansado(self):
    print "%s se sente cansado." % self.nome
    self.hp = max(1, self.hp - 1)
  def descansar(self):
    if self.estado != 'normal': print "%s não pode descansar agora!" % self.nome; self.ataque_inimigo()
    else:
      print "%s descansa." % self.nome
      if randint(0, 1):
        self.inimigo = Monstro(self)
        print "%s é rudemente acordado por %s!" % (self.nome, self.inimigo.nome)
        self.estado = 'luta'
        self.ataque_inimigo()
      else:
        if self.hp < self.hp_max:
            self.hp = self.hp + 1
        else: print "%s dormiu demais." % self.nome; self.hp = self.hp - 1
  def explorar(self):
    if self.estado != 'normal':
      print "%s está muito ocupado agora!" % self.nome
      self.ataque_inimigo()
    else:
      print "%s explora uma passagem assombrosa." % self.nome
      if randint(0, 1):
        self.inimigo = Monstro(self)
        print "%s encontra %s!" % (self.nome, self.inimigo.nome)
        self.estado = 'luta'
      else:
        if randint(0, 1): self.cansado()
  def fugir(self):
    if self.estado != 'luta':
        print "%s correm em círculos por um tempo." % self.nome
        self.cansado()
    else:
      if randint(1, self.hp + 5) > randint(1, self.inimigo.hp):
        print "%s foge de %s." % (self.nome, self.inimigo.nome)
        self.inimigo = None
        self.estado = 'normal'
      else:
        print "%s não escapou de %s!" % (self.nome, self.inimigo.nome)
        self.ataque_inimigo()
  def ataque(self):
    if self.estado != 'luta':
        print "%s soca o ar, aparentemente sem resultado." % self.nome
        self.cansado()
    else:
      if self.dano(self.inimigo):
        print "%s executa %s!" % (self.nome, self.inimigo.nome)
        self.inimigo = None
        self.estado = 'normal'
        if randint(0, self.hp) < 10:
          self.hp = self.hp + 1
          self.hp_max = self.hp_max + 1
          print "%s se sente mais forte!" % self.nome
      else: self.ataque_inimigo()
  def ataque_inimigo(self):
    if self.inimigo.dano(self):
        print "%s foi assassinado por %s!!!\nR.I.P." %(self.nome, self.inimigo.nome)
 
Comandos = {
  'sair': Jogador.sair,
  'ajuda': Jogador.ajuda,
  'status': Jogador.status,
  'descansar': Jogador.descansar,
  'explorar': Jogador.explorar,
  'fugir': Jogador.fugir,
  'atacar': Jogador.ataque,
  }
 
p = Jogador()
p.nome = raw_input("Qual o nome do seu personagem? ")
print "(digite ajuda para obter uma lista de ações)\n"
print "%s entra em uma caverna escurda, procurando por aventura." % p.nome
 
while(p.hp > 0):
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
      print "%s não sabe fazer isso." % p.nome