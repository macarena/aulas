class Raquete {
    constructor(player) {
        this.player = player;
        this.y = 10;
        this.w = 20;
        this.h = 100;
        this.v = 3;
        this.pts = 0;
        
        if (player) {
            this.x = 20;
            this.px = 50;
        } else {
            this.x = 800 - 20;
            this.px = 680;
        }
    }
    
    movimenta() {
        if(this.player) {
            this.y = mouseY;
        } else {
            //inteligência artificial
            if (bolinha.y > this.y && this.y < height - this.h/2)
                this.y+=this.v;
            if (bolinha.y < this.y && this.y > this.h/2)
                this.y-=this.v;
        }
        //pontos
        if ((bolinha.x > width && this.player) || (bolinha.x < 0 && !this.player)) {
            bolinha.reset();
            this.pts++;
        }
    }

    desenha() {
        this.movimenta();
        if (this.bateu()) {
            bolinha.bate();
        }
        rect(this.x,this.y,this.w,this.h);
        text(this.pts, this.px,height/2);
    }
    
    bateu() {
        //verificando X
        var distx = (this.w + bolinha.d)/2;
        if(Math.abs(bolinha.x - this.x) < distx) {   
            //verificando y
            var disty = (this.h + bolinha.d)/2;
            if(Math.abs(bolinha.y - this.y) < disty) {
                return true;
            }
        }
    }
}

bolinha = {
    x: 0,
    y: 0,
    vx: -4,
    vy: -4,
    d: 20,
    desenha: function() {
        this.movimenta();
        ellipse(this.x,this.y,this.d,this.d);
    },
    movimenta: function() {
        this.x += this.vx;
        this.y += this.vy;
        
        if(this.y + this.d/2 > height || this.y - this.d/2 < 0) {
            this.vy *= -1;
        }
    },
    reset: function() {
        this.x = width/2;
        this.y = height/2;
    },
    bate: function() {
        bolinha.vx *= -1;
    }
}

p1 = new Raquete(true);
p2 = new Raquete();

function setup() {
    createCanvas(800,600);
    noStroke();
    fill(255);
    bolinha.reset();
    rectMode(CENTER);
    textSize(94);
}

function draw() {
    background(0);
    p1.desenha();
    p2.desenha();
    bolinha.desenha();
}