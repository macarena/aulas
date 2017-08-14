#Brólistar - A estrelinha briguenta

w = 300
h = 300

bx = w/2
by = h/2
bs = 10
vel = 10

def setup():
    size(400,400, P3D)
    
def draw():
    background(0)
    fill(0,255,0)
    rect(0,0,w,h/2)
    
    fill(0,0,255)
    rect(0,h/2,w,h/2)
    
    fill(255,0,0)
    ellipse(bx,by,bs,bs)
    
    camera(bx, by,100, #olho
         bx,by,1, #bola
         0, 1, 0); #up

    
def keyPressed():
    global bx, by
    
    if keyCode == 37:
        bx -= vel
    if keyCode == 38:
        by -= vel
    if keyCode == 39:
        bx += vel
    if keyCode == 40:
        by += vel
        
    bx = constrain(bx,bs/2,w - bs/2)
    by = constrain(by,bs/2,h - bs/2)