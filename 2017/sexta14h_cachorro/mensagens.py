Class Mensageiro:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def novaMsg(self, mensagem):
        self.mensagem = mensagem
        
    def update(self):
        fill(0)
        rect(self.x, self.y, width, 30)
        fill(255)
        text(self.mensagem, self.x, self.y)
        
        