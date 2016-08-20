function setup() {
    createCanvas(800,600);
}

var x = 50;
var y = 50;
var speed = 5;
var raio = 40;

function draw() {
    
    background(255,123,50);
    noStroke();
    fill(255,0,0);
    ellipse(mouseX,mouseY,80,80);
    
    fill(0,0,255);
    ellipse(x,y,raio*2,raio*2);
    stroke(0);
    line(x,y,mouseX,mouseY);
    x = x + speed;
    
    if (x >= width-raio || x <= raio ) {
        speed = speed * -1;
    }
}