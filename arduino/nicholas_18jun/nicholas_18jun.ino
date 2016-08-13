int redi = 13;
int amareluweed = 12;
int verdidolly = 11;
int DYLM = 5;
int vallorr = 0;
int tenpu = 0;
int butum = 3;
int ystadubutum = 0;

void setup() {
  pinMode(redi,OUTPUT);
  Serial.begin(9600);
  pinMode(amareluweed,OUTPUT);
  pinMode(verdidolly,OUTPUT);
  pinMode(butum,INPUT);
  }
  // do you love me?

void loop() {
  vallorr = analogRead(DYLM);
  ystadubutum = digitalRead(butum);
  Serial.print(ystadubutum);

  digitalWrite(redi,HIGH);
  vallorr = analogRead(DYLM);
  tenpu = map(vallorr, 0, 1023, 70, 5000);
  delay(tenpu);
  digitalWrite(redi,LOW);

  if(ystadubutum == HIGH){
    digitalWrite(verdidolly,HIGH);
    vallorr = analogRead(DYLM);
    tenpu = map(vallorr, 0, 1023, 70, 5000);
    delay(tenpu);
    digitalWrite(verdidolly,LOW);
  }
  
  digitalWrite(amareluweed,HIGH);
  vallorr = analogRead(DYLM);
  tenpu = map(vallorr, 0, 1023, 70, 5000);
  delay(tenpu);
  digitalWrite(amareluweed,LOW);
}
