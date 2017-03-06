class Raquete {
    constructor(player) {
        this.player = player;
        this.y = 10;
        this.w = 20;
        this.h = 80;
        
        if (player) {
            this.x = 10;
        } else {
            this.x = 800 - 10 - this.w;
        }
    }
    
    movimenta() {
        if(this.player) {
            this.y = mouseY;
        } else {
            if (this.y > 0 && this.y < height - this.h) {
                if (bolinha.vy > 0 ) this.y++;
                if (bolinha.vy < 0 ) this.y--;
            }
        }
    }

    desenha() {
        this.movimenta();
        if (this.bateu()) {
            bolinha.bate();
        }
        rect(this.x,this.y,this.w,this.h);
    }
    
    bateu() {
        //verificando X
        var distancia = this.w + bolinha.d/2;
        if(bolinha.x >= this.x && bolinha.x <= this.x + distancia ) 
        {   
            //verificando y
            if(bolinha.y >= this.y && bolinha.y + this.h) {
                return true;
            }
        }
    }
}

bolinha = {
    x: 0,
    y: 0,
    vx: -2,
    vy: -2,
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
    stroke('white');
    strokeWeight(1);
    bolinha.reset();
}

function draw() {
    background(0);
    p1.desenha();
    p2.desenha();
    bolinha.desenha();
}