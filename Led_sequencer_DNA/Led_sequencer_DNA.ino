const int leds[] = {D0, D1, D2, D3};

const int greenled  = leds[0];
const int yellowled = leds[1];
const int redled    = leds[2];
const int blueled   = leds[3];

const int ON_DELAY = 300;
const int OFF_DELAY = 150;

const int DNA_sequence = ATGCGTACCTGATCGTAGCTAGGCTAACGTTGACCTAGCGTATCGGATCCGTAAGCTTGCATGCGTACGATCGTTAACGCGATGCTAGCTAGCATGGCCTA

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