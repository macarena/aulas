function Tabuleiro(navios) {
	this.tentativas = 0;
	this.escala = 50;

	this.colunas = 10;
	this.linhas = 10;
	this.casas = [];

	for (x=0;x<this.colunas;x++) {
		this.casas[x] = [];
		for (y=0;y<this.linhas;y++) {
			this.casas[x][y] = {
				navio: false,
				tentou: false,
			};
		}
	}

	this.desenha = function() {
		for (x=0;x<this.colunas;x++) {
			this.casas[x] = [];
			for (y=0;y<this.linhas;y++) {
				rect(x*this.escala,y*this.escala,this.escala,this.escala);
			}
		}
	}

	this.arrumar = function(navio) {
		var casa = false;
		do {
			linha = floor(Math.random()*this.linhas);
			coluna = floor(Math.random()*this.colunas);
			casa = this.casas[coluna][linha];
		} while (casa == true);
		this.casas[coluna][linha] = true;
		navio.posiciona(linha, coluna);
	}

	for (i=0;i<navios.length;i++){
		this.arrumar(navios[i]);
	}

	this.chute = function(x,y) {

	}
}

function Navio(nome, tamanho = 1, escala = 50) {
	this.nome = nome;
	this.vivo = true;
	this.tamanho = tamanho;
	this.escala = escala;

	this.posiciona = function(linha, coluna) {
		this.linha = linha;
		this.coluna = coluna;
	}

	this.desenha = function() {
		if (this.vivo) {
			ellipseMode('corner');
			ellipse(this.coluna*this.escala,this.linha*this.escala,this.escala,this.escala);
		}
		else {
			line(this.coluna*this.escala,this.linha*this.escala,this.coluna*this.escala + this.escala,this.linha*this.escala + this.escala);

		}
	}
}

var tabuleiro;
var navios = [];

function setup() {
	createCanvas(800,600);

	navios.push(new Navio("titanic"),new Navio("bote"),new Navio("barco"),new Navio("canoa"));
	tabuleiro = new Tabuleiro(navios);
}

function draw() {
	background(183,43,226);
	stroke(183,43,226);
	fill(255);
	tabuleiro.desenha();
	navios.forEach(function(navio){
		navio.desenha();
	});
}
