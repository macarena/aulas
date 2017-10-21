var img;
var x;
var y;
var w;
var h;
var bolinhas = [];

function setup() {
    img = loadImage('bandeira.jpg');
    createCanvas(innerWidth,innerHeight);
    noStroke();
    
    bolinha = {
        x: width / 2,
        y: height / 2,
        w: 500,
        h: 500,
        min: 10,
        cor: color(200),
        split: function() {
            w = this.w / 2;
            h = this.h / 2;
            if ( w < this.min ) { 
                return [this];
            }

            let bolinhas = [];
            for(let i=0; i < 4; i++) {
                bolinhas.push(Object.create(bolinha));
                bolinhas[i].w = w;
                bolinhas[i].h = h;
            }
            bolinhas[0].x = this.x-w/2;
            bolinhas[0].y = this.y-h/2;
            bolinhas[1].x = this.x+w/2;
            bolinhas[1].y = this.y-h/2;
            bolinhas[2].x = this.x-w/2;
            bolinhas[2].y = this.y+h/2;
            bolinhas[3].x = this.x+w/2;
            bolinhas[3].y = this.y+h/2;
            
            return bolinhas;
        }
    }
    
    bolinhas.push(bolinha);
}

function draw() {
    background(255);
    for(i=0; i<bolinhas.length; i++) {
        b = bolinhas[i];
        fill(b.cor);
        ellipse(b.x,b.y,b.w,b.h);

        if (dist(mouseX,mouseY,b.x,b.y) < b.w / 2) {
            novas = b.split();
            bolinhas.splice(i,1);
            Array.prototype.push.apply(bolinhas,novas);
        }
    }
}

function dist(ax, ay, bx, by) {
    dist = Math.sqrt((ax - bx)^2 + (ay - by)^2);
    return dist;
}