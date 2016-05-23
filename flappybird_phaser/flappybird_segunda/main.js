var jogo = new Phaser.Game(400, 490);

var estado = {
    preload: function() {
        //carregando imagem do passarinho
        jogo.load.image('passarinho', 'coisas/bird.png');
        
        //carregando imagem do cano
        jogo.load.image('quadrado', 'coisas/pipe.png');
    },
    
    create: function() {
        jogo.stage.backgroundColor = '#71c5cf';
        
        jogo.physics.startSystem(Phaser.Physics.ARCADE);
        
        this.passarinho = jogo.add.sprite(100, 245, 'passarinho');
        
        jogo.physics.arcade.enable(this.passarinho);
        
        this.passarinho.body.gravity.y = 1000;
        
        var espaco = jogo.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);
        
        espaco.onDown.add(this.pulo, this);
        
        //criando canos como grupo
        this.canos = jogo.add.group();
        
        //adiciona canos repetidas vezes em loop
        this.timer = jogo.time.events.loop(1500, this.addCano, this);
        
        //add placar
        this.placar = jogo.add.text(20, 20, "0", {
            font: "30px Arial Black",
            fill: "#fff"
        });
        
        this.pontos = 0;
        
        this.passarinho.anchor.setTo(-0.2, 0.5);
    },
    
    update: function() {
        if (this.passarinho.y > 490)
            this.reiniciaJogo();
        
        jogo.physics.arcade.overlap(this.passarinho, this.canos, this.reiniciaJogo);
        
        if(this.passarinho.angle < 20)
            this.passarinho.angle += 1;
    },
    
    reiniciaJogo: function() {
        jogo.state.start('main');
    },
    
    pulo: function() {
        this.passarinho.body.velocity.y = -350;
        
        var animacao = jogo.add.tween(this.passarinho);
        
        animacao.to({angle: -20},100);
        
        animacao.start();
    },
    
    addQuadrado: function(x,y) {
        //cria o sprite quadrado com a imagem quadrado
        var quadrado = jogo.add.sprite(x,y,'quadrado');
        
        //adicionar quadrado aos canos
        this.canos.add(quadrado);
        
        //colocando gravidade no quadrado
        jogo.physics.arcade.enable(quadrado);
        
        //colocando velocidade no quadrado
        quadrado.body.velocity.x = -200;
        
        //reconhece a tela e matar quadrado quando sair da tela
        quadrado.checkWorldBounds = true;
        quadrado.outOfBoundsKill = true;
    },
    
    addCano: function() {
        this.pontos += 1;// ganhando um ponto
        this.placar.text = this.pontos; //escrendo os pontos na tela
        
        //criando um buraco
        var buraco = Math.floor(Math.random() * 5) + 1;
        
        //criando 8 quadrados pra forma um cano
        for (var i = 0; i < 8; i++)
            if (i != buraco && i != buraco + 1)
                this.addQuadrado(400,10 + i*60);
    }

}

jogo.state.add('main', estado);
jogo.state.start('main');