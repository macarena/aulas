#Brólistar - A estrelinha briguenta
from personagem import *

w = 600
h = 600

def setup():
    global player
    size(400,400,P3D)
    player = Personagem(w/2,h/2,"sprite.png", w, h)
    
def draw():
    cx, cy = cameraMov(player.x,player.y,w,h)
    camera(cx, cy, 250, #olho
    cx,cy,1, #mira
    0, 1, 0); #up
    
    noStroke()
    background(0)
    
    fill(0,255,0)
    rect(0,0,w,h/2)
    
    fill(0,0,255)
    rect(0,h/2,w,h/2)
    
    player.update()
    
def keyPressed():
    if keyCode == 37:
        player.move('E')
    if keyCode == 38:
        player.move('C')
    if keyCode == 39:
        player.move('D')
    if keyCode == 40:
        player.move('B')
    
def keyReleased():
    if keyCode == 37:
        player.para('E')
    if keyCode == 38:
        player.para('C')
    if keyCode == 39:
        player.para('D')
    if keyCode == 40:
        player.para('B')
    
def cameraMov(x,y,w,h):
    margem = 140
    x = constrain(x, margem, w-margem)
    y = constrain(y, margem, h-margem)
    
    return x,y