function GotaDeChuva() {
    this.x = 50;
    this.y = -50;
    this.tam = 30;
    this.vel = 5;
    this.gros = 3;
    
    this.mostra = function () {
        strokeWeight(this.gros);
        line(this.x,this.y,this.x,this.y+this.tam);
    }
    
    this.cair = function () {
        //y = y + vel;
        this.y += this.vel;

        if (this.y > height) {
            this.y=-50;
        }
    }
}

var gota;

function setup () {
    createCanvas(900,650);
    gota = new GotaDeChuva();
}

function draw () {
    background(137,80,100);
    stroke(255);
    gota.mostra();
    gota.cair();
}