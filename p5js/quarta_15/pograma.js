function Raindrop() {
	this.x = random(800);
	this.y = random(-100,-20);
	this.h = 40;
	this.speed = random(5,10);

	this.fall = function () {
		this.y += this.speed;

		if (this.y > height) {
			this.y = random(-100,-20);
		}

	}

	this.show = function () {
		strokeWeight(3);
		stroke(255);
		line(this.x,this.y,this.x,this.y+this.h);
	}
}

var drops = [];

function setup() {
 	createCanvas(800,600);

	for (var i = 0; i < 500; i++) {
		drops[i] = new Raindrop();
	}
}

function draw() {
	background(183,43,226);
	for (var i = 0; i < 500; i++) {
		drops[i].show();
		drops[i].fall();
	}
}
