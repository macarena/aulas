class Muro:
    cor = color(200,100,0)
    estrutura = []
    
    def __init__(self, tamanho, w, h):
        self.s = tamanho
        for i in range(10):
            tijolo = PVector(0,i)
            self.estrutura.append(tijolo)
            
    def desenha(self):
        fill(self.cor)
        for tijolo in self.estrutura:
            x = tijolo.x * self.s
            y = tijolo.y * self.s
            rect(x,y,self.s,self.s)