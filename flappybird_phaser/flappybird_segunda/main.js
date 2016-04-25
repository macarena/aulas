var jogo = new Phaser.Game(400, 490);

var estado = {
    preload: function() {
        //carregando imagem do passarinho
        jogo.load.image('passarinho', 'coisas/bird.png');
    },
    
    create: function() {
        jogo.stage.backgroundColor = '#71c5cf';
        
        jogo.physics.startSystem(Phaser.Physics.ARCADE);
        
        this.passarinho = jogo.add.sprite(100, 245, 'passarinho');
        
        jogo.physics.arcade.enable(this.passarinho);
        
        this.passarinho.body.gravity.y = 1000;
        
        var espaco = jogo.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);
        
        espaco.onDown.add(this.pulo, this);
    },
    
    update: function() {
        
        if (this.passarinho.y > 490)
            this.reiniciaJogo();
    },
    
    reiniciaJogo: function() {
        jogo.state.start('main');
    },
    
    pulo: function() {
        this.passarinho.body.velocity.y = -350;
    }

}

jogo.state.add('main', estado);
jogo.state.start('main');