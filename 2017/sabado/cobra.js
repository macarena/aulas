tamanho = 600;
escala = 20;

function setup() {
    createCanvas(tamanho,tamanho);
    frameRate(8);
    
    cobrinha = {
        cor: color(255,0,0),
        corpo: [],
        dir: createVector(-20,0),
        cria: function() {
            for(i=0;i<4;i++) {
                x = tamanho / 2 + i*escala;
                y = tamanho / 2;
                q = createVector(x,y);
                this.corpo.push(q);
            }
        },
        desenha: function() {
            fill(this.cor);
            this.anda();
            for(i=0;i<this.corpo.length;i++) {
                q = this.corpo[i];
                rect(q.x,q.y,escala,escala);
            }
        },
        anda: function() {
            q = this.corpo[0].copy();
            q.add(this.dir);
            this.corpo.unshift(q);
            
            this.corpo.splice(-1,1);
        }
    };
    
    cobrinha.cria();
    
}

function draw() {
    background(0);
    cobrinha.desenha();
}