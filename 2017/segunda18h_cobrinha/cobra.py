class Cobra:
    corpo = []
    s = 10
    cor = color(0,255,0)
    
    def __init__(self):
        x= 600 / 2 / self.s
        y= 600 / 2 / self.s
        
        for i in range(4):
            q = {'x': x + i, 'y': y}
            self.corpo.append(q)
            
    def desenha(self):
        for qua in self.corpo:
            x = qua['x'] * self.s
            y = qua['y'] * self.s
            w = self.s
            h = self.s
            rect(x, y, w, h)