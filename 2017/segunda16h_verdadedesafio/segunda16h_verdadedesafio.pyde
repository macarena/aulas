participantes = ["Ana", "Marco", "Bia", "Julia", "Pedro"]
num = len(participantes)
angulo = 360 / num

def setup():
    size(400,400)

def draw():
    translate(width/2,height/2)
    x = 0
    y = 0
    w = 50
    h = 50
    #ellipse(x, y, w, h)
    
    for p in participantes:
        line(x,y,x,y-100)
        rotate(radians(angulo))