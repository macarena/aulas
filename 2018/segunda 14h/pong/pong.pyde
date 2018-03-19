#variáveis da bola
x=20
y=20
tamanho=10
vx=1
vy=-1
cor = color(255)

#raquete 1
r1x = 0
r1y = 0
r1w = 20
r1h = 100

#raquete 2
r2x = 0
r2y = 0
r2w = 20
r2h = 100



def setup():
    global x,y,r1x,r1y,r2x,r2y
    size(600,400)
    x=width/2
    y=height/2
    r1x=r1w/2 + 30
    r1y=height/2
    r2x=width-r2w/2-30
    r2y=height/2
    rectMode(CENTER)
    fill(cor)

def draw():
    global x,y,vy,vx,r2y
    x=x+vx
    y=y+vy
    
    r2y = constrain(mouseY, r2h/2, height-r2h/2)
    
    if y + tamanho/2 > height or y - tamanho/2 < 0:
        vy = vy * -1
         
    if x + tamanho/2 > width or x - tamanho/2 < 0:
        x = width/2
        y = height/2
        vx = vx * -1

    background(0)
    if passando(x,r2x):
        fill(255,0,0)
    else:
        fill(255)
    ellipse(x,y,tamanho,tamanho)

    rect(r1x,r1y,r1w,r1h)
    rect(r2x,r2y,r2w,r2h)
    
def keyPressed():
    global r1y
    
    if key == "w":
        r1y = constrain(r1y - 10, r1h/2, height-r1h/2)
    if key == "s":
        r1y = constrain(r1y + 10, r1h/2, height-r1h/2)
        
def passando(x1, x2):
    if abs(x1 - x2) < 25:
        return True
    else:
        return False
