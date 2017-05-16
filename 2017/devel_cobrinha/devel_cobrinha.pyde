from cobra import *
from comida import *

def setup():
    size(600,600)
    frameRate(8)
    
    global comida, cobrinha
    escala = 10
    comida = Comida(escala)
    cobrinha = Cobra(escala)
    
def draw():
    background(0)
    cobrinha.desenha(comida)
    comida.desenha()
    
def keyPressed():
    if keyCode == 37:
        v = PVector(-1,0)
        cobrinha.dir = v
    if keyCode == 38:
        v = PVector(0,-1)
        cobrinha.dir = v
    if keyCode == 39:
        v = PVector(1,0)
        cobrinha.dir = v
    if keyCode == 40:
        v = PVector(0,1)
        cobrinha.dir = v