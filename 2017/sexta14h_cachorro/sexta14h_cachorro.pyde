from mensagens import Mensageiro
from cachorro import Cachorro
from ui import ui

caramelo = color(139, 87, 66)

notif = Mensageiro(0,0)
dog = Cachorro("Totó", 4, caramelo, "macho", notif)


def setup():
    global img, interface
    size(600,400)
    interface = ui(dog)
    img = loadImage('cenario.png')
    
def draw():
    image(img, 0, 0, width, height)
    dog.update()
    notif.update()
    interface.update()
        
def mouseClicked():
    interface.mouseClicado()
    if dog.mouseover():
        dog.carinho()