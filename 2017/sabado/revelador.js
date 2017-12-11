var img;
var mouseXant;
var mouseYant;
var bolinhas = [];

var minX;
var minY;
var maxX;
var maxY;

var minXimg;
var minYimg;
var maxXimg;
var maxYimg;
var fundo;

var zise = 500;

function preload() {
    img = loadImage('revelador.jpg');
}

function setup() {
    fundo = color(255);

    createCanvas(innerWidth,innerHeight);
    noStroke();
    
    minX = width/2 - zise/2;
    maxX = width/2 + zise/2;
    minY = height/2 - zise/2;
    maxY = height/2 + zise/2;
    
    minXimg = 0;
    maxXimg = img.width;
    minYimg = 0;
    maxYimg = img.height;

    bolinha = {
        x: width / 2,
        y: height / 2,
        fx: width / 2,
        fy: height / 2,
        w: zise,
        h: zise,
        velox: 0,
        veloy: 0,
        min: 2,
        cor: color(200),
        movendo: function() {
            return !(this.x == this.fx && this.y == this.fy);
        },
        getColor: function() {
            x = map(this.fx, minX, maxX, minXimg, maxXimg);
            y = map(this.fy, minY, maxY, minYimg, maxYimg);
            this.cor = color(img.get(x,y));
        },
        animarAcelerado: function() {
            this.x += (this.fx - this.x) * 0.05 * 20;
            this.y += (this.fy - this.y) * 0.05;
        },
        animarRetilineo: function() {
            if(this.x != this.fx) {
                if (abs(this.fx - this.x) < abs(this.velox)) {
                    this.x = this.fx;
                } else {
                    this.x += this.velox;
                }
            }
            if(this.y != this.fy) {
                if (abs(this.fy - this.y) < abs(this.veloy)) {
                    this.y = this.fy;
                } else {
                    this.y += this.veloy;
                }
            }
        },
        getVelo() {
            this.velox = (this.fx - this.x) / 30;
            this.veloy = (this.fy - this.y) / 30;
        },
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
                bolinhas[i].x = this.x;
                bolinhas[i].y = this.y;
            }
            bolinhas[0].fx = this.x-w/2;
            bolinhas[0].fy = this.y-h/2;
            bolinhas[1].fx = this.x+w/2;
            bolinhas[1].fy = this.y-h/2;
            bolinhas[2].fx = this.x-w/2;
            bolinhas[2].fy = this.y+h/2;
            bolinhas[3].fx = this.x+w/2;
            bolinhas[3].fy = this.y+h/2;
            
            for(i=0;i<4;i++) {
                bolinhas[i].getColor();
                bolinhas[i].getVelo();
            }
            
            return bolinhas;
        }
    }
    
    bolinha.getColor();
    bolinhas.push(bolinha);
}

function draw() {
    background(fundo);
    for(let i=bolinhas.length-1; i >=0 ; i--) {
        let b = bolinhas[i];

        fill(b.cor);
        if (similiarColor(b.cor, fundo)) {
            stroke(200);
            strokeWeight(1);
        } else {
            noStroke();
        }
        b.animarRetilineo();    
        ellipse(b.x,b.y,b.w,b.h);
        
        if (!b.movendo()) {
            if (dist(mouseXant,mouseYant,b.x,b.y) > b.w / 2) {
                if (dist(mouseX,mouseY,b.x,b.y) < b.w / 2) {
                    novas = b.split();
                    bolinhas.splice(i,1);
                    Array.prototype.push.apply(bolinhas,novas);
                }
            }
        }
    }
    
    mouseXant = mouseX;
    mouseYant = mouseY;
}

function dist(ax, ay, bx, by) {
    dist = Math.sqrt((ax - bx)^2 + (ay - by)^2);
    return dist;
}

function similiarColor(cor_a, cor_b) {
    let a = cor_a.levels;
    let b = cor_b.levels;
    for(let i = 0; i < 4; i++) {
        if(abs(a[i] - b[i]) > 20) {
            return false;
        }
    }
    return true;
}
