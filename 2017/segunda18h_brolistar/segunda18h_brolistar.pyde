#Brólistar - A estrelinha briguenta
from personagem import *

w = 300
h = 300
player = Personagem(w/2,h/2,w,h)

def setup():
    size(400,400, P3D)
    
def draw():
    camera(player.x, player.y,100, #olho
        player.x,player.y,1, #bola
        0, 1, 0); #up
    
    background(0)
    fill(0,255,0)
    rect(0,0,w,h/2)
    fill(0,0,255)
    rect(0,h/2,w,h/2)
    
    player.update()
    
def keyPressed():
    player.move(keyCode)
    
def keyReleased():
    player.move(keyCode,True)
    
def cameraMov(x,y,w,h):
    margem = 140
    x = constrain(x, margem, w-margem)
    y = constrain(y, margem, h-margem)
    
    return x,y