function Gota() {
    this.x = random(width);
    this.y = random(-500,-50);
    this.z = random(0,20);
    this.tam = map(this.z, 0, 20, 10, 20);
    this.veloc = map(this.z, 0, 20, 1, 20);
    this.grossura = map(this.z, 0, 20, 1, 3);
    
    this.mostra = function() {
        strokeWeight(this.grossura);
        stroke(cor);
        line(this.x,this.y,this.x,this.y+this.tam);
    }
    
    this.cair = function() {
        this.y = this.y + this.veloc;
        var gravidade = map(this.z, 0, 20, 0, 0.2);
        this.veloc = this.veloc + gravidade;
        
        if (this.y > height) {
            this.y = random(-200,-100);
            this.veloc = map(this.z, 0, 20, 4, 10);
        }
    }
}

var gotas = [];
var fundo = 255;
var cor = [183,43,226];

function setup() {
    createCanvas(1020,650);
    for (var i = 0; i < 500; i++) {
        gotas[i] = new Gota();
    }
}

function draw() {
    background(fundo);
    for (var i = 0; i < gotas.length; i++) {
        gotas[i].cair();
        gotas[i].mostra();
    }
    if (mouseIsPressed) {
        fundo = 255;
        cor = [183,43,226];
    } else {
        fundo = [183,43,226];
        cor = 255;
    }
}