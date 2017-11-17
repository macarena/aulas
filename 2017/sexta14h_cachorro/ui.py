class ui:
    def __init__(self, cachorro):
        self.cachorro = cachorro
    
    def update(self):
        #barrinha de felicidade
        self.barrinha(10,50,self.cachorro.felicidade)
        
        #barrinha de fome
        self.barrinha(10,60,self.cachorro.fome, color(0,255,0))

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