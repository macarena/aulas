from cobra import *

c = Cobra()

def setup():
  size(600,600)
  frameRate(10)

def draw():
  background(0)
  c.desenha()
  
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
        