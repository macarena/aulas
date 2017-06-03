tamanho = 600;
escala = 20;

function setup() {
    createCanvas(tamanho,tamanho);
    
    cobrinha = {
        cor: color(255,0,0),
        corpo: [],
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
            for(i=0;i<this.corpo.length;i++) {
                q = this.corpo[i];
                rect(q.x,q.y,escala,escala);
            }
        }
    };
    
    cobrinha.cria();
    
}

function draw() {
    background(0);
    cobrinha.desenha();
}