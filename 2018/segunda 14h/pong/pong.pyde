cor = color(255)

#variáveis da bola
x=0
y=0
tamanho=10
vx=1
vy=-1

#raquete 1
r1x = 0
r1y = 0
r1w = 20
r1h = 100
r1p = 0

#raquete 2
r2x = 0
r2y = 0
r2w = 20
r2h = 100
r2p = 0

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
    textAlign(CENTER, CENTER)
    textSize(130)
    fill(cor)

def draw():
    global x,y,vy,vx,r2y,r1p,r2p
    
    #movendo a bolinha
    x+=vx
    y+=vy
    
    #movendo a raquete 2
    r2y = constrain(mouseY, r2h/2, height-r2h/2)
    
    #rebatendo bolinha em cima e embaixo
    if y + tamanho/2 > height or y - tamanho/2 < 0:
        vy *= -1
         
    #resetando a bolinha se bater nas laterais (GOL)
    if x + tamanho/2 > width:
        x = width/2
        y = height/2
        vx *= -1
        r1p += 1
    if x - tamanho/2 < 0:
        x = width/2
        y = height/2
        vx *= -1
        r2p += 1
        
    #rebatendo nas raquetes
    margemX = (tamanho+r2w)/2
    margemY = (tamanho+r2h)/2
    if batendo(x,y,r1x,r1y,margemX,margemY) or batendo(x,y,r2x,r2y,margemX,margemY):
        vx = vx * -1
    
    #desenhando tudo
    background(0)
    text(r1p, 150, 50)
    text(r2p, width - 150, 50)
    ellipse(x,y,tamanho,tamanho)
    rect(r1x,r1y,r1w,r1h)
    rect(r2x,r2y,r2w,r2h)
    
    
def keyPressed():
    global r1y
    #movendo a raquete 1
    if key == "w":
        r1y = constrain(r1y - 10, r1h/2, height-r1h/2)
    if key == "s":
        r1y = constrain(r1y + 10, r1h/2, height-r1h/2)
        
def batendo(x1, y1, x2, y2, margemX, margemY):
    return abs(x1 - x2) < margemX and abs(y1 - y2) < margemY