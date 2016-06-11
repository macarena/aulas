int vermelho = 13;
int amarelo = 12;
int verde = 11;
int meus_pinos[] = {13, 12, 11};
int qt_pinos = 3;
int potPin = 0; //pino do potenciometro
int pot = 0; //valor do potenciomentro

int semaforo (int pinos[], int qt, int tempo) {
  for (int pino = 0; pino < qt; pino++){
    digitalWrite(pinos[pino], HIGH);
    delay(tempo);
    digitalWrite(pinos[pino], LOW);
  }
}

void setup()
{
  Serial.begin(9600);
  for (int pino = 0; pino < qt_pinos; pino++){
    pinMode(meus_pinos[pino], OUTPUT);
  }
}

void loop()
{
  pot = analogRead(potPin);
  int tempo = map(pot,0,1023,74,5000);
  semaforo(meus_pinos,qt_pinos,tempo);
}
