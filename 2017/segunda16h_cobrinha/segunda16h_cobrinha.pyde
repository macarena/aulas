from cobra import *
from comida import *
from muro import *

def setup():
  global f, c, m
  size(600,600)
  frameRate(10)
  m = Muro(width,height)
  f = Comida(m,width,height)
  c = Cobra(f,m,width,height)
  
def draw():
  background(0)
  m.desenha()
  c.desenha()
  f.desenha()
  
  
def keyPressed():
    if keyCode == 37 and c.dir != PVector(1,0):
        #esquerda
        c.dir = PVector(-1,0)
        
    if keyCode == 38 and c.dir != PVector(0,1):
        #cima
        c.dir = PVector(0,-1)
        
    if keyCode == 39 and c.dir != PVector(-1,0):
        #direita
        c.dir = PVector(1,0)
        
    if keyCode == 40 and c.dir != PVector(0,-1):
        #baixo
        c.dir = PVector(0,1)
        