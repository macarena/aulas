participantes = ["Ana", "Marco", "Bia", "Julia", "Pedro"]
num = len(participantes)
angulo = 360 / num
giro = 0
velocidade = 0
freio = -0.1
selecionados = []

def setup():
    global garrafa, cor
    size(400,400)
    garrafa = loadImage("garrafa.png")
    cor = color(random(255),random(255),random(255))
    imageMode(CENTER)

def draw():
    global bt1, selecionados
    background(cor)
    
    bt1 = addBotao("Roda Garrafa", 50,50,100,20)
    if velocidade == 0 and selecionados:
        textAlign(LEFT,TOP)
        text(selecionados[0] + " pergunta para " + selecionados[1], 50, 80)
    
    translate(width/2,height*2/3)
    x = 0
    y = 0
    
    for p in participantes:
        line(x,y,x,y-100)
        rotate(radians(angulo/2))
        
        if p in selecionados:
            fill(255,0,0) 
            textSize(20)
        else:
            fill(0)
            textSize(12)
        textAlign(CENTER,CENTER)
        text(p,0,-100)
        rotate(radians(angulo/2))
    
    selecionados = rodaGarrafa()
    print(selecionados)
        
def rodaGarrafa():
    global giro, velocidade, freio
    selecionados = []
    
    rotate(radians(giro))
    image(garrafa, 0, 0, 45, 133)
    giro += velocidade
    velocidade += freio
    
    if giro > 360:
        giro = 0
        
    if velocidade <= 0:
        velocidade = 0
        freio = 0

    selecionados.append(participantes[int(giro/angulo)])
    outro = int((giro+180)/angulo)
    selecionados.append(participantes[outro] if outro < 5 else participantes[outro-5])
        
    return selecionados
        
def addBotao(texto, btx, bty, btw, bth):
    fill(20,130,210)
    rect(btx, bty, btw, bth)
    fill(0)
    textSize(12)
    textAlign(CENTER,CENTER)
    text(texto, btx + btw/2, bty + bth/2)
    
    if btx < mouseX < btx + btw and bty < mouseY < bty + bth:
        return True
    else:
        return False
    
def mouseClicked():
    if bt1:
        global velocidade, freio
        velocidade = velocidade + random(5,10)
        freio = random(-0.5,-0.1)
        