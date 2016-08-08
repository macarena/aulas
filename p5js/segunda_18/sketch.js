function Gota() {
    this.x = random(width);
    this.y = random(-100,-20);
    this.tam = random(20,60);
    this.veloc = random(5,15);
    
    this.mostra = function() {
        line(this.x,this.y,this.x,this.y+this.tam);
    }
    
    this.cair = function() {
        this.y = this.y + this.veloc;
        
        if (this.y > height) {
            this.y = random(-100,-20);
        }
    }
}

var gotas = [];

function setup() {
    createCanvas(1280,800);
    for (var i = 0; i < 500; i++) {
        gotas[i] = new Gota();
    }
}

function draw() {
    background(255);
    for (var i = 0; i < gotas.length; i++) {
        gotas[i].cair();
        gotas[i].mostra();
    }
}