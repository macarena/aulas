from mensagens import Mensageiro
from cachorro import Cachorro

caramelo = color(139, 87, 66)

notif = Mensageiro(0,0)
dog = Cachorro("Totó", 4, caramelo, "macho", notif)

def setup():
    global img
    size(600,400)
    img = loadImage('cenario.png')
    
def draw():
    image(img, 0, 0, width, height)
    dog.update()
    notif.update()
    
def keyPressed():
    if key == ' ':
        dog.comer()