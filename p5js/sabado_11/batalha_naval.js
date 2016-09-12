function Navio(nome) {
    this.nome = nome;
    this.vivo = true;
    this.tamanho = 1;
    this.escala = 50;
    
    this.posiciona = function (linha, coluna) {
        this.linha = linha;
        this.coluna = coluna;
        this.x = coluna * this.escala;
        this.y = linha * this.escala; 
    }
    
    this.desenha = function () {
        if (this.vivo) {
            //desenhar bola
            ellipse(this.x,this.y,this.escala,this.escala);
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
            this.casas[x][y] = {tentou: false,navio: false};
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
    
    this.arrumar = function (navio) {
        do {
            linha = floor(Math.random() * this.linhas);
            coluna = floor(Math.random() * this.colunas);
            casa = this.casas[coluna][linha];
        } while (casa.navio != false);
        casa.navio = navio;
        navio.posiciona(linha,coluna);
    }
    
    for (i=0;i<navios.length;i++) {
        this.arrumar(navios[i]);
    }
}
var t;
var n = [];

function setup() {
    createCanvas(800,600);
    n.push(new Navio("titanic"), new Navio("bote"));
    t = new Tabuleiro(n);
}

function draw() {
    t.desenha();
}