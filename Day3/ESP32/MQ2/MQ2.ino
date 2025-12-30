int mq2Pin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int gasValue = analogRead(mq2Pin);
  Serial.print("Gas Value: ");
  Serial.println(gasValue);

  if (gasValue > 400) {
    Serial.println("⚠ GAS DETECTED!");
  }

  delay(1000);
}
