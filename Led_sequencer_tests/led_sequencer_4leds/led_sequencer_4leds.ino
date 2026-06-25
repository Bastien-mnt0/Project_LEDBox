const int leds[] = {D0, D1, D2, D3};
const int NB_LEDS = 4;

void setup() {
  for (int i = 0; i < NB_LEDS; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], HIGH);
  }
}

void loop() {

}
