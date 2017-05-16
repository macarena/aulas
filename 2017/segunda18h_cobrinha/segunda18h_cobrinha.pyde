from cobra import *

c = Cobra()

def setup():
    size(600,600)
    frameRate(10)
    
def draw():
    background(0)
    c.desenha()
    
def keyPressed():
    esquerda = PVector(-1,0)
    direita = PVector(1,0)
    baixo = PVector(0,1)
    cima = PVector(0,-1)
    
    if keyCode == 37 and c.dir != direita:
        #esquerda
        c.dir = esquerda
    if keyCode == 38 and c.dir != baixo:
        #cima
        c.dir = cima
    if keyCode == 39 and c.dir != esquerda:
        #direita
        c.dir = direita
    if keyCode == 40 and c.dir != cima:
        #baixo
        c.dir = baixo
        