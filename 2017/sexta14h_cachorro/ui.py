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
    
    def update(self):
        #barrinha de felicidade
        self.barrinha(10,50,self.cachorro.felicidade)
        
        #barrinha de fome
        self.barrinha(10,60,self.cachorro.fome, color(0,255,0))
        
        #botões de comida
        x = 400
        for comida in self.comidas:
            self.botao(x,350,self.cachorro.comer, arg = comida["valor"])
            x += 50

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
        
    def botao(self, x, y, callback, arg, cor = color(200,200,255)):
        stroke(30)
        strokeWeight(1)
        fill(cor)
        w = 50
        h = 50
        rect(x, y, w, h)
        dx = mouseX - x
        dy = mouseY - y
        
        if mousePressed:
            if dx >= 0 and dx <= w:
                if dy >= 0 and dy <= h:
                    callback(arg)