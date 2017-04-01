var quadradinho = {
    s: 25,
    bomba: false,
    proximidade: 0,
    revelado: false,
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
        if (!this.relevado) {
            fill(120,180,255);
            rect(this.x,this.y,this.s,this.s);
        }
    },
};

var tabuleiro = [];

var colunas = 20;
var linhas = 20;

for (c = 0; c < colunas; c++){
    for (l = 0; l < linhas; l++){
        q = Object.create(quadradinho);
        q.goto(c,l);
        tabuleiro.push(q);
    }
}


function setup() {
    createCanvas(800,600);
}

function draw() {
    background(255);
    tabuleiro.forEach(function(q) {
        q.d();
    });
}

function mousePressed() {
    tabuleiro.forEach(verificaClique);
}

function verificaClique(q) {
    cliqueX = int(mouseX / q.s);
    cliqueY = int(mouseY / q.s);

    if (cliqueX == q.col && cliqueY == q.lin) {
        q.revelado = true;
    }
}