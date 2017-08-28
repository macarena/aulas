participantes = ["Ana", "Marco", "Bia", "Julia", "Pedro", "Joana", "Rafael", "Flavia", "Paulo", "Beto", "David", "Luciana"]
num = len(participantes)
angulo = 360 / num
giro = 0
velocidade = 0
freio = -0.1
nome = ""

def setup():
    global garrafa, cor
    size(400,400)
    garrafa = loadImage("garrafa.png")
    cor = color(random(255),random(255),random(255))
    imageMode(CENTER)

def draw():
    background(cor)
    global botao1, botao2, botao3
    botao1 = criaBtn("Play", 50, 50, 50, 50)
    botao2 = criaBtn("-", 300, 50, 20, 20)
    botao3 = criaBtn("+", 350, 50, 20, 20)
    input = criaInput(nome, 50, 350, 200, 20)
    
    translate(width/2,height/2)
    x = 0
    y = 0
    
    for p in participantes:
        line(x,y,x,y-100)
        rotate(radians(angulo/2))
        textAlign(CENTER,CENTER)
        text(p, x, y - 100)
        rotate(radians(angulo/2))

    giraGarrafa()

def giraGarrafa():
    global giro, velocidade, freio
    rotate(radians(giro))
    image(garrafa, 0, 0, 45, 133)
    giro += velocidade
    velocidade += freio
    
    if giro > 360:
        #módulo % é o resto da divisão
        giro = giro % 360
        
    if velocidade <= 0:
        velocidade = 0
        
def criaBtn(texto, x, y, w, h):
    fill(0,200,0)
    ellipse(x,y,w,h)
    fill(0)
    textAlign(CENTER,CENTER)
    text(texto, x, y)
    
    d = sqrt(pow(mouseX-x, 2) + pow(mouseY-y, 2))
    
    if d < w/2:
        return True
    else:
        return False

def delPessoa():
    global num, angulo
    if len(participantes) > 1:
        del participantes[-1]
        num = len(participantes)
        angulo = 360 / num
        
def addPessoa():
    global num, angulo, nome
    participantes.append(nome)
    num = len(participantes)
    angulo = 360 / num
    nome = ""
    
    
def mouseClicked():
    if botao1:
        global velocidade
        velocidade += random(5,10)
    if botao2:
        delPessoa()
    if botao3:
        addPessoa()
        
def criaInput(texto, x, y, w, h):
    fill(255)
    rect(x,y,w,h)
    fill(0)
    textAlign(LEFT,TOP)
    text(texto, x, y)
    
def keyPressed():
    global nome
    if keyCode == 8:
        nome = nome[:-1]
    elif type(key) is unicode:
        nome += str(key)