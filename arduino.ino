void setup() {
  Serial.begin(115200);
}

void loop() {
  int a = analogRead(A0);
  int b = analogRead(A1);
  int c = analogRead(A2);
  int d = analogRead(A3);
  Serial.print(a);
  Serial.print(" , ");
  Serial.print(b);
  Serial.print(" , ");
  Serial.print(c);
  Serial.print(" , ");
  Serial.println(d);
  delay(100);
}