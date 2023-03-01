void setup() {
  Serial.begin(115200);
}

void loop() {
  if (Serial.available()) {
    // Read the incoming data
    String data = Serial.readString();

    // Print the data out at a lower baud rate
    Serial.begin(9600);
    Serial.println(data);
    Serial.end();
    Serial.begin(115200);
  }
}
