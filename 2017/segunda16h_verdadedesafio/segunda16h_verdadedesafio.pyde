participantes = ["Ana", "Marco", "Bia", "Julia", "Pedro"]
num = len(participantes)
angulo = 360 / num
giro = 0
velocidade = 50
freio = -0.1

def setup():
    global garrafa, cor
    size(400,400)
    garrafa = loadImage("garrafa.png")
    cor = color(random(255),random(255),random(255))
    imageMode(CENTER)

def draw():
    global giro, velocidade, freio
    background(cor)
    
    translate(width/2,height/2)
    x = 0
    y = 0
    w = 50
    h = 50
    
    for p in participantes:
        line(x,y,x,y-100)
        rotate(radians(angulo))
    
    rotate(radians(giro))
    image(garrafa, 0, 0, 45, 133)
    giro += velocidade
    velocidade += freio
    
    if giro > 360:
        giro = 0
        
    if velocidade <= 0:
        velocidade = 0
        freio = 0