#coding: utf-8

class Cachorro:
    def __init__(self, nome, idade, cor, sexo, patas = 4):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.sexo = sexo
        self.patas = patas
        self.fome = 0
        self.felicidade = 100
        self.sono = 0
        
    def __repr__(self):
        return "Este eh o cachorro " + self.nome + ". Ele tem " + str(self.idade) + " anos."
    
    def comer(self):
        if self.fome > 30:
            self.fome -= 20
            notif.novaMsg(self.nome + " está mais feliz")
        else:
            notif.novaMsg(self.nome + " não quer comer...")
            
    def update(self):
        global height, width
        x = width/2
        y = height * 3/4
        w = 10 * self.idade
        h = w * 2/3
        fill(self.cor)
        ellipse(x,y,w,h)
        rectMode(CENTER)
        
        self.fome += 0.01
        self.fome = constrain(self.fome,0,100)
        rect(x,y-h,100 - self.fome,8)
        
        self.felicidade -= 0.01
        self.felicidade = constrain(self.felicidade, 0, 100)
        rect(x,y-h-15,self.felicidade,5)