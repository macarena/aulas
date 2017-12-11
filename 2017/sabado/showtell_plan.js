var bolinhas = [];

function setup() {
    createCanvas(600,400);
    b = {
        move: function() {
            this.x += this.vx;
            this.y += this.vy;
            if (this.x >= width - this.tamanho/2 || this.x <= this.tamanho/2) {
                this.vx *= -1;
            }
            if (this.y >= height - this.tamanho/2 || this.y <= this.tamanho/2) {
                this.vy *= -1;
            }
        },
        cria: function(x, y) {
            this.x = x;
            this.y = y;
            this.cor = color(random(255),random(255),random(255));
            this.tamanho = random(10,50);
            this.vx = random(-5,5);
            this.vy = random(-5,5);
        }
    };
    b.cria(width/2, height/2);
    bolinhas.push(b);
}

function draw() {
    background(0);
    bolinhas.forEach(function(b){
        fill(b.cor);
        ellipse(b.x, b.y, b.tamanho, b.tamanho);
        b.move();
    });
}

function mouseClicked() {
    let nova = Object.create(b);
    nova.cria(mouseX, mouseY);
    bolinhas.push(nova);
}