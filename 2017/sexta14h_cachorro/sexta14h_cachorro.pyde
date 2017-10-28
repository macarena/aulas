from mensagens import Mensageiro
from cachorro import Cachorro
from ui import ui

caramelo = color(139, 87, 66)

notif = Mensageiro(0,0)
dog = Cachorro("Totó", 4, caramelo, "macho", notif)
interface = ui(dog)

def setup():
    global img
    size(600,400)
    img = loadImage('cenario.png')
    
def draw():
    image(img, 0, 0, width, height)
    dog.update()
    notif.update()
    interface.update()
    
def keyPressed():
    if key == ' ':
        dog.comer()