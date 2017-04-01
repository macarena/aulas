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
			for (y=0;y<this.linhas;y++) {
				rect(x*this.escala,y*this.escala,this.escala,this.escala);
			}
		}
	}

	this.arrumar = function(navio) {
		do {
			linha = floor(Math.random()*this.linhas);
			coluna = floor(Math.random()*this.colunas);
			casa = this.casas[coluna][linha];
		} while (casa.navio == true);
		this.casas[coluna][linha] = navio;
		navio.posiciona(linha, coluna);
	}

	for (i=0;i<navios.length;i++){
		this.arrumar(navios[i]);
	}

	this.chute = function(x,y) {
		m.mensagem("Você chutou "+this.tentativas+" vezes");
		linha = Math.floor(x/this.escala);
		coluna = Math.floor(y/this.escala);
		m.mensagem('chutando em ' + linha + '|' + coluna);

		if (this.fora(linha,coluna)) {
			m.mensagem("Você chutou fora do tabuleiro");
			return;
		}

		if (this.repetido(linha,coluna)) {
			m.mensagem("Você já tentou aí");
			return;
		}

		this.tentativas++;

		m.mensagem("Tiro disparado...");

		if (this.casas[linha][coluna] instanceof Navio) {
			m.mensagem("Parabéns!");
			this.casas[linha][coluna].vivo = false;
		} else {
			m.mensagem("Você errou!");
			this.casas[linha][coluna].tentou = true;
		}
	}

	this.fora = function (linha,coluna) {
		if (linha < 0 || linha >= this.linhas) {
            return true;
		}
        if (coluna < 0 || coluna >= this.colunas){
            return true;
        }
        return false;
	}

	this.repetido = function(x,y) {
		if (this.casas[x][y].tentou == true) {
			return true;
		}
		return false;
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

function Mural () {
	this.texto = [];
	this.mensagem = function (texto) {
		this.texto += texto + '\n';
	}
	this.desenha = function () {
		text(this.texto, 510,10,790,200);
	}
}

var tabuleiro;
var navios = [];

function setup() {
	createCanvas(800,501);

	navios.push(new Navio("titanic"),new Navio("bote"),new Navio("barco"),new Navio("canoa"));
	tabuleiro = new Tabuleiro(navios);
	m = new Mural();
}

function draw() {
	background(183,43,226);
	stroke(183,43,226);
	fill(255);
	tabuleiro.desenha();
	navios.forEach(function(navio){
		navio.desenha();
	});
	m.desenha();
}

function mouseClicked() {
	tabuleiro.chute(mouseX,mouseY);
}