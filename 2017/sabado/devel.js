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
        if (mouseIsPressed) {
            this.c();
        }
        
        if (!this.revelado) {
            fill(120,180,255);
            rect(this.x,this.y,this.s,this.s);
        } else if (this.bomba) {
            fill(255,80,50);
            rect(this.x,this.y,this.s,this.s);
        } else if (this.proximidade > 0) {
            fill(255);
            stroke(200);
            rect(this.x,this.y,this.s,this.s);
            fill(0);
            text(this.proximidade, this.x + this.s/2, this.y+this.s-5);
        } else {
            fill(255);
            stroke(200);
            rect(this.x,this.y,this.s,this.s);
        }
    },
    c: function() {
        col = int(clicado.x / this.s);
        lin = int(clicado.y / this.s);

        if (col == this.col && lin == this.lin) {
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

var tabuleiro = [];

var colunas = 20;
var linhas = 20;

var clicado = {x: -1, y: -1};
var qtb = 40;

for (c = 0; c < colunas; c++){
    for (l = 0; l < linhas; l++){
        q = Object.create(quadradinho);
        q.goto(c,l);
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
    clicado.x = mouseX;
    clicado.y = mouseY;
}

function mouseReleased() {
    clicado.x = -1;
    clicado.y = -1;
}