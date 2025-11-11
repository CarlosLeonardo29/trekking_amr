// Leitura do pino 2 com detecção de BORDA DE SUBIDA e DEBOUNCE
// Envia o estado atual da GPIO via Serial

#include <Wire.h>
#include <SparkFun_APDS9960.h>

SparkFun_APDS9960 apds;

const byte ENC_PIN = 2;
const unsigned long debounceDelay = 1; // tempo mínimo em ms para validar a mudança

int lastStableState = HIGH;  // último estado confirmado
int lastReading = HIGH;      // última leitura bruta
unsigned long lastChangeTime = 0;

// Pinos I2C ESP32
const int SDA_PIN = 21;
const int SCL_PIN = 22;

#define RELE_PIN 5

int amareloUntil = 0; 

void setup() {
  Serial.begin(115200);
  pinMode(ENC_PIN, INPUT_PULLUP);
  pinMode (RELE_PIN, OUTPUT);

  lastStableState = lastReading = digitalRead(ENC_PIN);

  Wire.begin(SDA_PIN, SCL_PIN);
}

void loop() {
  unsigned long now = millis();
  int currentReading = digitalRead(ENC_PIN);

  uint16_t R, G, B, C;

  // lê os valores brutos
  apds.readRedLight(R);
  apds.readGreenLight(G);
  apds.readBlueLight(B);
  apds.readAmbientLight(C);

  // soma dos três canais
  uint32_t somaRGB = (uint32_t)R + (uint32_t)G + (uint32_t)B;

  

  if (somaRGB >= 2500){
    digitalWrite(RELE_PIN, LOW);
  } else {
    digitalWrite(RELE_PIN, HIGH);
  }
  

  // Se a leitura mudou, reinicia o temporizador de debounce
  if (currentReading != lastReading) {
    lastReading = currentReading;
    lastChangeTime = now;
  }

  // Se o sinal ficou estável por mais que debounceDelay ms, considera válido
  if ((now - lastChangeTime) > debounceDelay) {
    if (currentReading != lastStableState) {
      // Detecta BORDA DE SUBIDA (LOW -> HIGH)
      if (lastStableState == LOW && currentReading == HIGH) {
        Serial.println(currentReading);
      }
      // Atualiza o estado estável
      lastStableState = currentReading;
    }
  }
  
}