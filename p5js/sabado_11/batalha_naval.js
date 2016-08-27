function Navio(nome) {
    this.nome = nome;
    this.vivo = true;
    this.tamanho = 1;
    this.escala = 50;
    
    this.posiciona = function (linha, coluna) {
        this.linha = linha;
        this.coluna = coluna;
    }
    
    this.desenha = function () {
        if (this.vivo) {
            //desenhar bola
        } else {
            //desenhar X ou bola vermelha
        }
    }
}

function Tabuleiro(navios) {
    this.tentativas = 0;
    this.linhas = 10;
    this.colunas = 10;
    this.casas = [];
    this.escala = 50;
    
    for (x=0; x<this.colunas; x++) {
        this.casas[x] = [];
        for (y=0; y<this.linhas; y++) {
            this.casas[x][y] = {tentou: false};
        }
    }
    
    this.desenha = function () {
        for (l = 0; l < this.linhas; l++) {
            for (c = 0; c < this.colunas; c++) {
                w = this.escala;
                h = this.escala;
                x = c * this.escala;
                y = l * this.escala;
                rect(x,y,w,h);
            }
        }
    }  
}
var t;
var n = [];

function setup() {
    createCanvas(800,600);
    n.push(new Navio("titanic"));
    t = new Tabuleiro(n);
}

function draw() {
    t.desenha();
}