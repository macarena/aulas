function setup() {
    createCanvas(640,480);
    
}

var batata = 50;
var min_batata = 50;
var max_batata = 250;

function draw() {
    
    background(255,255,255);
    fill(255,0,0);
    noStroke();
    //essa linha faz uma bola vermelha
    ellipse(mouseX, mouseY, batata, batata);
    //batata = batata + 1;
    
}

function mouseClicked() {
    if (mouseX < width/2) {
        if (batata > min_batata) {
            somaBatata(-5, "diminuindo");
        } else {
            console.log("Não é possível diminuir mais");
        }
    } else {
        if (batata < max_batata) {
            somaBatata(5, "aumentando");
        } else {
            console.log("Não é possível aumentar mais");
        }
    }
}

function somaBatata(numero, texto) {
    batata = batata + numero;
    console.log(texto + " para " + batata);
}