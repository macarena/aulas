var numLinhas;
var bolas;
var vel;
var raio;
var fundo;

function setup() {
    createCanvas(500,500,WEBGL);
    fundo = loadImage('bandeira.jpg');
    
    numLinhas = 10;
    bolas = 10;
    raio = 20;
    vel = 0.0000005;
}

function draw() {
    background(200);
    fill (255);
    
    //texture(fundo);
    //rx = map(mouseX, 0, width, 0, 360);
    //ry = map(mouseY, 0, height, 360, 0);
    //rotateY(radians(rx));
    //rotateX(radians(ry));
    //box(200, 200, 200);
    beginShape();
    vertex(30, 75);
    vertex(40, 20);
    vertex(50, 75);
    endShape(CLOSE);
    /*
    for (var linha = 0; linha < numLinhas; linha++){

        
        beginShape(TRIANGLE_STRIP);
        
        for (var col = 0; col < bolas; col++){
            var cx = map(col, 0, bolas, 0, width);
            var cy = map(linha, 0, numLinhas, 0, height);
            var nx = map(col, 0, bolas, 0, width);
            var ny = map(linha+1, 0, numLinhas, 0, height);
            
            var distCentro = dist(cx, cy, width/2, height/2);
            var an = frameCount * vel + distCentro*0.02 + col*0.1;
            
            var x = cx + raio * cos(an);
            var y = cy + raio * sin(an);
            vertex(x, y);

            var distCentro = dist(nx, ny, width/2, height/2);
            var an = frameCount * vel + distCentro*0.02 + col*0.1;
                        
            var x = nx + raio * cos(an);
            var y = ny + raio * sin(an);
            vertex(x, y);

        }
        
    }
    */
    
}