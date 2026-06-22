const int leds[] = {D0, D1, D2, D3};
const int NB_LEDS = 4;

const int DELAI_ALLUME = 300;
const int DELAI_ETEINT = 150;

void setup() {
  for (int i = 0; i < NB_LEDS; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }
}

void loop() {
  for (int i = 0; i < NB_LEDS; i++) {
    digitalWrite(leds[i], HIGH);
    delay(DELAI_ALLUME);

    digitalWrite(leds[i], LOW);
    delay(DELAI_ETEINT);
  }
}