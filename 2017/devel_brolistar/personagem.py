class Personagem:
    dirs = {
            'C':False,
            'B':False,
            'D':False,
            'E':False
            }
    
    def __init__(self, x, y, arquivo_sprite, w, h):
        self.x = x
        self.y = y
        self.s = 10
        self.vel = 2
        self.w = w
        self.h = h
        self.dir = 0
        self.sprite = loadImage(arquivo_sprite)
        self.geraSprites()
        
    def update(self):
        if self.dirs['C']:
            self.y = self.y - self.vel
            self.dir = 3
        if self.dirs['B']:
            self.y = self.y + self.vel
            self.dir = 0
        if self.dirs['E']:
            self.x = self.x - self.vel
            self.dir = 1
        if self.dirs['D']:
            self.x = self.x + self.vel
            self.dir = 2
        
        self.x = constrain(self.x,self.s/2, self.w - self.s/2)
        self.y = constrain(self.y,self.s/2, self.h - self.s/2)
        
        self.desenha()
        
    def move(self, dir):
        self.dirs[dir] = True
        
    def para(self, dir):
        self.dirs[dir] = False
        
    def desenha(self):
        w = self.sprite.width/3
        h = self.sprite.height/4
        
        if self.pos >= 2.5 or self.pos <= 0.5:
            self.posMove *= -1
        self.pos += self.posMove
        pos = int(self.pos)
        
        fill(255,0,0)
        ellipse(self.x,self.y,5,5)
        self.colocaSprite(pos)
        
    def colocaSprite(self,pos):
        img = self.imgs[self.dir][pos]
        x = self.x - img.width/2
        y = self.y - img.height + 10
        
        image(img, x, y)
        
    def geraSprites(self):
        cols = 3
        lins = 4
        w = self.sprite.width/cols
        h = self.sprite.height/lins
        self.pos = 1
        self.posMove = 0.1
        
        self.imgs = []
        
        for i in range(lins):
            linha = []
            for j in range(cols):
                linha.append(self.sprite.get(w*j, h*i, w, h))
            self.imgs.append(linha)