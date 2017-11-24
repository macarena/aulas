#coding: utf-8

class Mensageiro:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mensagem = ''
        
    def novaMsg(self, mensagem):
        self.mensagem = mensagem
        
    def update(self):
        fill(0,0,0,120)
        noStroke()
        rectMode(CORNER)
        h = 30
        rect(self.x, self.y, width, h)
        fill(255)
        textAlign(LEFT,CENTER)
        margem = 20
        x = self.x + margem
        y = self.y + h / 2
        text(self.mensagem, x , y)