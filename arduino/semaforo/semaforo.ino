//simples
int vermelho = 13;
int amarelo = 12;
int verde = 11;
int tempo = 2000;

//complexo
int meus_pinos[] = {vermelho, amarelo, verde};
int qt_pinos = 3;

int semaforo (int pinos[], int qt, int tempo) {
  for (int pino = 0; pino < qt; pino++){
    digitalWrite(pinos[pino], HIGH);
    delay(tempo*1000);
    digitalWrite(pinos[pino], LOW);
  }
}

void setup()
{
  for (int pino = 0; pino < qt_pinos; pino++){
    pinMode(meus_pinos[pino], OUTPUT);
  }
}

void loop()
{
  /* modo simples
  digitalWrite(vermelho, HIGH);
  delay(tempo);
  digitalWrite(vermelho, LOW);
  digitalWrite(amarelo, HIGH);
  delay(tempo);
  digitalWrite(amarelo, LOW);
  digitalWrite(verde, HIGH);
  delay(tempo);
  digitalWrite(verde, LOW);
  */
  
  //modo complexo
  semaforo(meus_pinos,qt_pinos,1);
}
