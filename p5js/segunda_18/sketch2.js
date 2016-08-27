var bolaA = {
    x: 50,
    y: 50,
};

var bolaB = {x: 500, y: 300};
var bolaC = {x: 50, y: 300};

function setup() {
    createCanvas(600,400);
}

function draw() {
    background(130,158,32);
    ellipse(bolaA.x,bolaA.y,80,80);
    ellipse(bolaB.x,bolaB.y,40,40);
    ellipse(bolaC.x,bolaC.y,50,50);
    
    line(bolaA.x,bolaA.y,bolaB.x,bolaB.y);
    line(bolaB.x,bolaB.y,bolaC.x,bolaC.y);
    line(bolaC.x,bolaC.y,bolaA.x,bolaA.y);
    
    
    bolaC.x = mouseX;
    bolaC.y = mouseY;
    
    bolaA.x = bolaA.x + 1;
    bolaB.y = bolaB.y + 1;
}