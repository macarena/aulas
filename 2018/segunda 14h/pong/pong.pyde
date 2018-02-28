#variáveis da bolinha
x = 20
y = 20
tamanho = 15
cor = color(255)

def setup():
    global x, y
    size(600,400)
    x = width / 2
    y = height / 2
    rectMode(CENTER)
    
def draw():
    background(0)
    fill(cor)
    ellipse(x,y,tamanho,tamanho)