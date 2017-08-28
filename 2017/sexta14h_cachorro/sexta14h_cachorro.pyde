class Cachorro:
    def __init__(self, nome, idade, cor, sexo, patas = 4, fome = True):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.sexo = sexo
        self.patas = patas
        self.fome = fome
        
    def __repr__(self):
        return "Este eh o cachorro " + self.nome + ". Ele tem " + str(self.idade) + " anos."
    
    def comer(self):
        if self.fome:
            print (self.nome + " está mais feliz")
        else:
            print (self.nome + " não quer comer...")

dog = Cachorro("Totó", 4, "caramelo", "macho")
tadinho = Cachorro("Rex", 10, "preto", "macho", 2, False)

dog.comer()
tadinho.comer()