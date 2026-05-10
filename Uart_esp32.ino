void setup() {
  Serial.begin(115200); // Même vitesse que sur le PC
  pinMode(2, OUTPUT);   // Pour tester avec la LED
}

void loop() {
  // Vérifie si des données sont arrivées
  if (Serial.available() > 0) {
    // Lit le message jusqu'au caractère de fin de ligne
    String message = Serial.readStringUntil('\n');
    message.trim(); // Nettoie les espaces/caractères invisibles

    Serial.print("ESP32 a reçu : ");
    Serial.println(message);

    // Action simple : si on reçoit "ON", on allume la LED
    if (message == "ON") {
      digitalWrite(2, HIGH);
    } else if (message == "OFF") {
      digitalWrite(2, LOW);
    }
  }
}
