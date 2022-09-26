void setup() {
  Serial.begin(115200);
}

void loop() {
  int a = analogRead(A0);
  int b = 5;
  Serial.print(b);
  Serial.print(" , ");
  Serial.println(a);
  delay(500);
}