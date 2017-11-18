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
        min: 2,
        cor: color(200),
        getColor: function() {
            x = map(this.fx, minX, maxX, minXimg, maxXimg);
            y = map(this.fy, minY, maxY, minYimg, maxYimg);
            this.cor = color(img.get(x,y));
            this.similar = similarColors(this.cor, fundo);
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
                bolinhas[i].animating = true;
            }
            bolinhas[0].fx = this.x-w/2;
            bolinhas[0].fy = this.y-h/2;
            bolinhas[1].fx = this.x+w/2;
            bolinhas[1].fy = this.y-h/2;
            bolinhas[2].fx = this.x-w/2;
            bolinhas[2].fy = this.y+h/2;
            bolinhas[3].fx = this.x+w/2;
            bolinhas[3].fy = this.y+h/2;
            
            bolinhas[0].getColor();
            bolinhas[1].getColor();
            bolinhas[2].getColor();
            bolinhas[3].getColor();
            
            return bolinhas;
        },
        desenha: function() {
            if(this.animating) {
                this.x = moveTo(this.x, this.fx, this.w / 20);
                this.y = moveTo(this.y, this.fy, this.w / 20);
                if (this.fx == this.x) {
                    this.animating = false;
                }
            }
            
            if (this.sumindo) {
                let transp = alpha(this.cor) - 50;
                this.cor = color(red(this.cor),green(this.cor),blue(this.cor), transp);
                if (transp <= 0) {
                    //bolinhas.splice(this.sumindo,1);
                    this.sumindo = false;
                }
            }
            
            if (this.similar) {
                stroke(200);
                strokeWeight(1);
            } else {
                noStroke();
            }

            fill(this.cor);
            ellipse(this.x,this.y,this.w,this.h);
        },
        animating: false,
        sumindo: false,
    }
    
    bolinha.getColor();
    bolinhas.push(bolinha);
}

function draw() {
    background(fundo);
    for(let i=bolinhas.length-1; i >=0 ; i--) {
        let b = bolinhas[i];
        b.desenha();
        if(!b.animating && !b.sumindo) {
            if (dist(mouseXant,mouseYant,b.x,b.y) > b.w / 2) {
                if (dist(mouseX,mouseY,b.x,b.y) < b.w / 2) {
                    //setTimeout(splitBolinha(b,i),1);
                    splitBolinha(b);
                }
            }
        }
        
        if (alpha(b.cor) == 0) {
            bolinhas.splice(i,1);
        }
    }
    mouseXant = mouseX;
    mouseYant = mouseY;
}

function dist(ax, ay, bx, by) {
    dist = Math.sqrt((ax - bx)^2 + (ay - by)^2);
    return dist;
}

function splitBolinha(b) {
    novas = b.split();
    b.sumindo = true;
    Array.prototype.push.apply(bolinhas,novas);
}

function similarColors(cor_a, cor_b) {
    let a = cor_a.levels;
    let b = cor_b.levels;

    for(let i = 0; i < 3; i++) {
        if(abs(a[i] - b[i]) > 15) {
            return false;
        }
    }
    
    return true;
}

function moveTo(s,d,vel) {
    if (abs(d-s) < vel) {
        return d;
    }
    if (d > s) {
        return s + vel;
    } else {
        return s - vel;
    }
}