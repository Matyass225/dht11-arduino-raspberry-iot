#include <Wire.h>
#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11
#define SLAVE_ADDR 0x08

DHT dht(DHTPIN, DHTTYPE);
float t, h;

void setup() {
  dht.begin();
  Wire.begin(SLAVE_ADDR); 
  Wire.onRequest(requestEvent); // Akkor fut le, ha a Pi adatot kér
}

void loop() {
  t = dht.readTemperature();
  h = dht.readHumidity();
  delay(2000); // A DHT11-nek idő kell
}

void requestEvent() {
  byte data[2];
  data[0] = (byte)t; // Hőmérséklet (egész rész)
  data[1] = (byte)h; // Páratartalom (egész rész)
  Wire.write(data, 2); 
}