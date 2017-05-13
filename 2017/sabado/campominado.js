//modelo do quadrado
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
        if (!this.revelado) {
            fill(120,180,255);
            rect(this.x,this.y,this.s,this.s);
        } else {
            fill(255);
            if (this.bomba) { fill(255,0,0); }
            rect(this.x,this.y,this.s,this.s);
            if (this.proximidade > 0) {
                fill(0);
                text(this.proximidade, this.x + this.s/2, this.y + this.s/2);
            }
        }
    },
    vizinhos: function() {
        vizinhos = [];
        for (i = 0; i < tabuleiro.length; i++) {
            if ((tabuleiro[i].col >= this.col-1 && tabuleiro[i].col <= this.col +1) && (tabuleiro[i].lin >= this.lin-1 && tabuleiro[i].lin <= this.lin +1) && !(tabuleiro[i].lin == this.lin && tabuleiro[i].col == this.col)) {
                vizinhos.push(tabuleiro[i]);
            }
        }
        return vizinhos;
    },
    revelar: function() {
        if(!this.revelado && !this.bomba) {
            this.revelado = true;
            if(this.proximidade == 0) {
                vizinhos = this.vizinhos();
                vizinhos.forEach(function(q){
                    q.revelar();
                });
            }
        }
        
        if(this.bomba && !this.revelado) {
            this.revelado = true;
            tabuleiro.forEach(function(q) {
               if(q.bomba) {
                   q.revelar();
               } 
            });
        }
    }
};

//tabuleiro vazio
var tabuleiro = [];

//info de quantas colunas e quantas linha eu quero
var colunas = 20;
var linhas = 20;

//loop de criação do tabuleiro
//populando o tabuleiro com quadradinho
for (c = 0; c < colunas; c++){
    for (l = 0; l < linhas; l++){
        q = Object.create(quadradinho);
        q.goto(c,l);
        tabuleiro.push(q);
    }
}

//colocando bombas
var qtb = 30;

while (qtb > 0) {
    var target = tabuleiro.length;
    var aleatorio = Math.random() * target;
    var qbomba = Math.floor(aleatorio);
    if(!tabuleiro[qbomba].bomba) {
        tabuleiro[qbomba].bomba = true;
        vizinhos = tabuleiro[qbomba].vizinhos();
        vizinhos.forEach(function(v) {
            v.proximidade++;
        });
        qtb--;
    }
}

function setup() {
    createCanvas(800,600);
    textAlign(CENTER,CENTER);
}

function draw() {
    background(255);
    //loop para desenhar os quadradinhos do tabuleiro
    tabuleiro.forEach(function(q) {
        q.d();
    });    textAlign(CENTER,CENTER);

}

function mousePressed() {
    tabuleiro.forEach(verificaClique);
}

function verificaClique(q) {
    cliqueX = Math.floor(mouseX / q.s);
    cliqueY = Math.floor(mouseY / q.s);

    if (cliqueX == q.col && cliqueY == q.lin) {
        //q.revelado = true;
        q.revelar();
    }
}