var bolinhas = [];

function criarBolinhas() {
    let bola = {
        vx: Math.random() * 8,
        vy: Math.random() * 8,
        r: Math.random() * 25,
        x: Math.random() * (800 - this.r*2) + this.r,
        y: Math.random() * (600 - this.r*2) + this.r,
        cor: color(Math.random() * 255,Math.random() * 255,Math.random() * 255)
    };
    return bola;
}

function setup(){
    createCanvas(800, 600);
    for(let n=0; n < 100; n++){
        bolinhas.push(criarBolinhas());
    }
}

function draw() {
    background(0);  
    
    for(let i = 0; i < bolinhas.length; i++) {
        fill(bolinhas[i].cor);
        ellipse(bolinhas[i].x,bolinhas[i].y,bolinhas[i].r*2,bolinhas[i].r*2);
        bolinhas[i].x = bolinhas[i].x+bolinhas[i].vx;
        bolinhas[i].y = bolinhas[i].y+bolinhas[i].vy;
        if(bolinhas[i].x >= width-bolinhas[i].r || bolinhas[i].x <= bolinhas[i].r){
            bolinhas[i].vx = bolinhas[i].vx * -1;
        }
        if(bolinhas[i].y >= height-bolinhas[i].r || bolinhas[i].y <= bolinhas[i].r){
            bolinhas[i].vy = bolinhas[i].vy * -1;
        }
    }
}