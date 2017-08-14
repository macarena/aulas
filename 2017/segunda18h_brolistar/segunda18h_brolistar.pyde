#Brólistar - A estrelinha briguenta

bx = 0
by = 0
vel = 10

w = 500
h = 800

def setup():
    size(100,100, P3D)
    
def draw():
    background(0)
    fill(0,255,0)
    rect(0,0,w,h)
    
    fill(255,0,0)
    ellipse(bx,by,10,10)
    
    camera(bx, by,100, #olho
         bx,by,1, #bola
         0, 1, 0); #up

    
def keyPressed():
    global bx, by, vel
    
    if keyCode == 37:
        bx -= vel
    if keyCode == 38:
        by -= vel
    if keyCode == 39:
        bx += vel
    if keyCode == 40:
        by += vel
