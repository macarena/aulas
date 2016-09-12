var q = [];
s = 50;
var clique = {};

function setup() {
    createCanvas(800,600);
    
    for (l=0;l<10;l++) {
        for (c=0;c<10;c++) {
            q.push({
                x: c * s,
                y: l * s,
                l: l,
                c: c,
                chute: false
            });
        }
    }
}

function draw() {
    for(i=0;i<q.length;i++){
        rect(q[i].x,q[i].y,s,s);
        
        if (q[i].chute) {
            line(q[i].x,q[i].y,q[i].x+s,q[i].y+s);
            line(q[i].x+s,q[i].y,q[i].x,q[i].y+s);
        }
        
        if (q[i].l == clique.l && q[i].c == clique.c) {
            q[i].chute = true;
        }
    }
}

function mouseClicked() {
    linha = Math.floor(mouseY / s);
    coluna = Math.floor(mouseX / s);
    
    if (linha < 10 && coluna < 10) {
        //cliquei dentro do tabuleiro
        clique = {l: linha, c: coluna};
    }
}