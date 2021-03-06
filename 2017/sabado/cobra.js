tamanho = 600;
escala = 20;

function setup() {
    createCanvas(tamanho,tamanho);
    frameRate(10);
    
    comida = {
        x: Math.floor(random(0,tamanho/escala)) * escala,
        y: Math.floor(random(0,tamanho/escala)) * escala,
        cor: color(0,255,0),
        comeu: function() {
            this.x = Math.floor(random(0,tamanho/escala)) * escala;
            this.y = Math.floor(random(0,tamanho/escala)) * escala;
        },
        desenha: function() {
            fill(this.cor);
            rect(this.x,this.y, escala, escala);
        }
    }
    
    cobrinha = {
        cor: color(255,0,0),
        corpo: [],
        dir: createVector(0,0),
        viva: true,
        cria: function() {
            for(i=0;i<4;i++) {
                x = tamanho / 2 + i*escala;
                y = tamanho / 2;
                q = createVector(x,y);
                this.corpo.push(q);
            }
            this.setDir(dirs['a']);
        },
        desenha: function() {
            fill(this.cor);
            if (this.viva) this.anda();
            for(i=0;i<this.corpo.length;i++) {
                q = this.corpo[i];
                rect(q.x,q.y,escala,escala);
            }
        },
        anda: function() {
            if (this.tempDir) this.setDir(this.tempDir);
            
            q = this.corpo[0].copy();
            q.add(this.dir);
            this.corpo.unshift(q);
            
            //teletransporte
            if (this.corpo[0].x < 0) {
                this.corpo[0].x = tamanho - escala;
            }
            if (this.corpo[0].x >= tamanho) {
                this.corpo[0].x = 0;
            }
            if (this.corpo[0].y < 0) {
                this.corpo[0].y = tamanho - escala;
            }
            if (this.corpo[0].y >= tamanho) {
                this.corpo[0].y = 0;
            }
            
            //morreu batendo nela mesma
            for(i=1;i<this.corpo.length;i++) {
                if(this.corpo[0].dist(this.corpo[i]) == 0) {
                    this.viva = false;
                    this.cor = color(0,0,255);
                }
            }
            
            //comendo
            if (this.corpo[0].x == comida.x && this.corpo[0].y == comida.y) {
                comida.comeu();
            } else { 
                this.corpo.splice(-1,1);
            }
        },
        setDir: function(d) {
            angulo = degrees(p5.Vector.angleBetween(this.dir,d));
            if (angulo != 180) {
                this.dir = d.copy();
                this.dir.mult(escala);
            }
        }
    };
    
    dirs = {
        'w' : createVector(0,-1),
        'a' : createVector(-1,0),
        's' : createVector(0,1),
        'd' : createVector(1,0)
    };

    cobrinha.cria();
    
}   

function draw() {
    background(0);
    cobrinha.desenha();
    comida.desenha();
}

function keyPressed() {
    switch(key.toLowerCase()) {
        case 'w':
        case 'a':
        case 's':
        case 'd':
            d = dirs[key.toLowerCase()]
            cobrinha.tempDir = d
            break;
    }
}