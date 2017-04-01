function setup() {
    createCanvas(800,600);
}

q = [];
s = 20;

for (l=0;l<10;l++) {
    for (c=0;c<10;c++) {
        x = c * s;
        y = l * s;
        
        q.push({
            x: x,
            y: y,
            c: c,
            l: l,
            navio: false,
            chute: false
        });
    }
}

function draw() {
    background(255);
    for (i=0;i<q.length;i++) {
        rect(q[i].x,q[i].y,s,s);
        if(q[i].chute) {
            line(q[i].x,q[i].y,q[i].x+s,q[i].y+s);
            line(q[i].x,q[i].y+s,q[i].x+s,q[i].y);
        }
    }
}

function mouseClicked() {
    coluna = floor(mouseX / s);
    linha = floor(mouseY / s);
    
    for (i=0;i<q.length;i++) {
        if(q[i].l == linha && q[i].c == coluna) {
            q[i].chute = true;
        }
    }
}