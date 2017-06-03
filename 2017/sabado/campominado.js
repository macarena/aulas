//modelo do quadrado
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
            fill(120,180,255);
            if(this.marcado) {
                fill(0,250,100);
            }
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
            this.marcado = false;
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
            gameover = true;
        }
    },
    desarmar: function() {
        if (this.marcado) {
            this.marcado = false;
        } else {
            if (marcadas < qtb && !this.revelado) {
                this.marcado = true;
            }
        }
    }
};

//tabuleiro vazio
var tabuleiro = [];
var gameover = false;

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
var bombas = qtb;

while (bombas > 0) {
    var target = tabuleiro.length;
    var aleatorio = Math.random() * target;
    var qbomba = Math.floor(aleatorio);
    if(!tabuleiro[qbomba].bomba) {
        tabuleiro[qbomba].bomba = true;
        tabuleiro[qbomba].proximidade = -1;
        vizinhos = tabuleiro[qbomba].vizinhos();
        vizinhos.forEach(function(v) {
            if(!v.bomba) {
                v.proximidade++;
            }
        });
        bombas--;
    }
}

function setup() {
    createCanvas(800,600);
    textAlign(CENTER,CENTER);
}

function draw() {
    marcadas = 0;
    for(i = 0; i < tabuleiro.length; i++) {
        if (tabuleiro[i].marcado) {
            marcadas++;
        }
    }
    
    background(255);
    textAlign(CENTER,CENTER);
    //loop para desenhar os quadradinhos do tabuleiro
    textSize(12);
    tabuleiro.forEach(function(q) {
        q.d();
    });
    
    textAlign(LEFT,CENTER);
    fill(0);
    text(qtb + " bombas no tabuleiro", 520, 20);
    text(marcadas + " bombas marcadas", 520, 40);
    
    
    textAlign(CENTER,CENTER);
    if (gameover) {
        textSize(80);
        fill(255,0,0);
        text("Game Over",width/2,height/2);
    }
    
    if(verificaVitoria()) {
        textSize(80);
        fill(255,0,0);
        text("You WON",width/2,height/2);
    }
}

function mousePressed() {
    if (!gameover) tabuleiro.forEach(verificaClique);
}

function verificaClique(q) {
    cliqueX = Math.floor(mouseX / q.s);
    cliqueY = Math.floor(mouseY / q.s);

    if (cliqueX == q.col && cliqueY == q.lin) {
        //q.revelado = true;
        q.revelar();
    }
}

function verificaDesarme(q) {
    cliqueX = Math.floor(mouseX / q.s);
    cliqueY = Math.floor(mouseY / q.s);

    if (cliqueX == q.col && cliqueY == q.lin) {
        q.desarmar();
    }
}

function keyPressed() {
    if (key == ' ' && !gameover) {
        tabuleiro.forEach(verificaDesarme);
    }
}

function verificaVitoria() {
    listabombas = [];
    for(i=0;i<tabuleiro.length;i++) {
        if(tabuleiro[i].bomba) {
            listabombas.push(tabuleiro[i]);
        }
    }

    for(i=0;i<listabombas.length;i++) {
        if(!listabombas[i].marcado) {
            return false;
        }
    }
    
    return true;
}