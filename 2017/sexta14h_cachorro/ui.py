#coding: utf-8

class ui:
    def __init__(self, cachorro):
        self.cachorro = cachorro
        self.comidas = [
                        {"nome": "biscoito", "valor": 5},
                        {"nome": "bife", "valor": 15},
                        {"nome": "ração", "valor": 10},
                        {"nome": "lixo", "valor": -2}
                        ]
        self.elementos = []
        
        #botões de comida
        x = 400
        for comida in self.comidas:
            b = Botao(x,350)
            b.definirCallback(self.cachorro.comer, comida["valor"])
            if comida["nome"] == "biscoito":
                b.definirImagem('biscoito.png')
            self.elementos.append(b)
            x += 50
            
        b = Botao(0,350)
        b.definirCallback(self.cachorro.brincar)
        self.elementos.append(b)
        
    
    def update(self):
        #barrinha de felicidade
        self.barrinha(10,50,self.cachorro.felicidade)
        
        #barrinha de fome
        self.barrinha(10,60,self.cachorro.fome, color(0,255,0))
        
        for elemento in self.elementos:
            elemento.update()

    def mouseClicado(self):
        for elemento in self.elementos:
            dx = mouseX - elemento.x
            dy = mouseY - elemento.y

            if dx >= 0 and dx <= elemento.w:
                if dy >= 0 and dy <= elemento.h:
                    elemento.clicado()

    def barrinha(self, x, y, qtd, cor = color(255,0,0)):
        tamanho = 250
        grossura = 8
        pre = map(qtd,0,100,0,tamanho)
        
        stroke(30)
        strokeWeight(1)
        fill(255)
        rect(x,y,tamanho,grossura)
        
        noStroke()
        fill(cor)
        rect(x,y,pre,grossura)
                    
class Botao:
    w = 50
    h = 50
    cor = color(200,200,200)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def definirCallback(self, func, *args):
        self.callback = func
        self.callback_args = args
    
    def definirImagem(self, url):
        self.img = loadImage(url)
                          
    def update(self):
        stroke(30)
        strokeWeight(1)
        fill(self.cor)
        rect(self.x, self.y, self.w, self.h)
        if hasattr(self, 'img'):
            image(self.img, self.x, self.y, self.w, self.h)
        
    def clicado(self):
        if hasattr(self, 'callback'):
            self.callback(*self.callback_args)