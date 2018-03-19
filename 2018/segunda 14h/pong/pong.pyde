#variáveis da bolinha
x = 0
y = 0
vx = 1
vy = -1
tamanho = 15
cor = color(255)

#variáveis da raquete 1
R1x = 0
R1y = 0
R1w = 20
R1h = 100

#variáveis da raquete 2
R2x = 0
R2y = 0
R2w = 20
R2h = 100

def setup():
    global x, y, R1x, R1y, R2x, R2y
    size(600,400)
    x = width / 2
    y = height / 2
    R1x = R1w/2 + 30
    R1y = height / 2
    R2x = width - R2w/2 - 30
    R2y = height / 2
    rectMode(CENTER)
    fill(cor)
    
def draw():
    global x, y, vy
    x = x + vx
    y = y + vy
    
    if y + tamanho / 2 > height or y - tamanho / 2 < 0:
        vy = vy * -1
        
    background(0)
    ellipse(x,y,tamanho,tamanho)
    rect(R1x, R1y, R1w, R1h)
    rect(R2x, R2y, R2w, R2h)
