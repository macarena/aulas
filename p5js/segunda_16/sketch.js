function setup() {
    createCanvas(640,480);
    
}

var batata = 50;

function draw() {
    
    background(255,255,255);
    fill(255,0,0);
    noStroke();
    //essa linha faz uma bola vermelha
    ellipse(mouseX, mouseY, batata, batata);
    //batata = batata + 1;
}