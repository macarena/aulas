var quadradinho = {
    s: 25,
    bomba: false,
    proximidade: 0,
    revelado: false,
    marcado: false,
    col: 0,
    lin: 0,
    x:0,
    y:0,
    goto: function(col,lin) {
        this.col = col;
        this.lin = lin;
        this.x = col * this.s;
        this.y = lin * this.s;
    },
    d: function() {
        if (!this.revelado) {
            stroke(0);
            if (this.marcado) {
                fill(255,80,50);
                rect(this.x,this.y,this.s,this.s);
            } else {
                fill(120,180,255);
                rect(this.x,this.y,this.s,this.s);
            }
        } else if (this.bomba) {
            console.log("Game Over");
        } else {
            fill(255);
            stroke(200);
            rect(this.x,this.y,this.s,this.s);
            if (this.proximidade > 0) {
                fill(0);
                text(this.proximidade, this.x + this.s/2, this.y+this.s-5);
            }
        }
    },
    c: function(marcar = false) {
        if (marcar) {
            this.marcado = !this.marcado;
        } else {
            this.revelar();
        }
    },
    revelar: function () {
        if (!this.revelado) {
            this.revelado = true;
            if (this.proximidade == 0) {
                this.perto().forEach(function(q){
                   q.revelar();
                });
            }
        }
    },
    perto: function() {
        let lista = [];
        let ref = this;
        tabuleiro.forEach(function(q){
            if(q.col >= ref.col-1 &&
               q.col <= ref.col+1 &&
               q.lin >= ref.lin-1 &&
               q.lin <= ref.lin+1 &&
               !(q.col == ref.col &&
               q.lin == ref.lin)) {
                lista.push(q);
            }
        });
        return lista;
    },
    colocaBomba: function() {
        this.bomba = true;
        this.perto().forEach(function(q){
           q.proximidade += 1; 
        });
    }
};

var tamanho = 25;
var tabuleiro = [];
var colunas = 20;
var linhas = 20;
var qtb = 40;

for (c = 0; c < colunas; c++){
    for (l = 0; l < linhas; l++){
        q = Object.create(quadradinho);
        q.goto(c,l);
        q.s = tamanho;
        tabuleiro.push(q);
    }
}

function soma(s,q) {
    if (q.bomba) {
        return s+1;
    } else {
        return s;
    }
}

while(tabuleiro.reduce( soma , 0) < qtb) {
    n = Math.floor(Math.random() * tabuleiro.length);
    //tabuleiro[n].bomba = true;
    tabuleiro[n].colocaBomba();
}

function setup() {
    createCanvas(800,600);
    textSize(16);
    textStyle(BOLD);
    textAlign(CENTER);
}

function draw() {  
    background(255);
    tabuleiro.forEach(function(q) {
        q.d();
    });
}

function mousePressed() {
    col = int(mouseX / tamanho);
    lin = int(mouseY / tamanho);
    
    tabuleiro.forEach(function(q) {
        if (col == q.col && lin == q.lin) {
            q.c();
        }
    });
}

function keyPressed() {
    if (keyCode == 32) {
        col = int(mouseX / tamanho);
        lin = int(mouseY / tamanho);

        tabuleiro.forEach(function(q) {
            if (col == q.col && lin == q.lin) {
                q.c(true);
            }
        });
    }
}