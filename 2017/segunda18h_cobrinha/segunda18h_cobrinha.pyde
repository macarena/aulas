from cobra import *
from comida import *
from muro import *

tamanho = 10

def setup():
    global f, c, m
    size(600,600)
    frameRate(10)
    m = Muro(tamanho,width,height)
    f = Comida(tamanho, width, height)
    c = Cobra(tamanho, f, m, width, height)
    
def draw():
    background(0)
    c.desenha()
    f.desenha()
    m.desenha()
    
def keyPressed():
    esquerda = PVector(-1,0)
    direita = PVector(1,0)
    baixo = PVector(0,1)
    cima = PVector(0,-1)
    
    if keyCode == 37 and c.dir != direita:
        #esquerda
        c.dir = esquerda
    elif keyCode == 38 and c.dir != baixo:
        #cima
        c.dir = cima
    elif keyCode == 39 and c.dir != esquerda:
        #direita
        c.dir = direita
    elif keyCode == 40 and c.dir != cima:
        #baixo
        c.dir = baixo