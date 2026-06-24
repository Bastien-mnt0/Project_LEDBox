const int redled    = D0;
const int blueled   = D1;
const int greenled  = D2;
const int yellowled = D3;

const int NB_LEDS = 4;
const int leds[]  = { redled, blueled, greenled, yellowled };

const int ON_DELAY  = 300;
const int OFF_DELAY = 150;

const char* DNA_sequences[] = {
  "TGCACAGGGACATGCACAGGCTTTCAGGATGAAGGCCAGGNACATCGCAAGAAGCGATTTCATCAGGATG",
  "ATGTTTNNGACAAGCAGGGACTACGGAAAAAAATGTGGGCG",
};

const int NB_SEQ = 2;

void transition() {
  for (int i = 0; i < NB_LEDS; i++) digitalWrite(leds[i], LOW);
  delay(500);
  for (int i = 0; i < NB_LEDS; i++) digitalWrite(leds[i], HIGH);
  delay(2000);
  for (int i = 0; i < NB_LEDS; i++) digitalWrite(leds[i], LOW);
  delay(500);
}

void setup() {
  randomSeed(analogRead(A0));
  for (int i = 0; i < NB_LEDS; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }
}

void loop() {
  
  transition();
  
  const char* seq = DNA_sequences[random(NB_SEQ)];

  for (int i = 0; i < (int)strlen(seq); i++) {
    char base = seq[i];
    int  led  = -1;

    switch (base) {
      case 'A': led = redled;    break;
      case 'T': led = blueled;   break;
      case 'G': led = greenled;  break;
      case 'C': led = yellowled; break;
      default: break;
    }

    if (led != -1) {
      digitalWrite(led, HIGH);
      delay(ON_DELAY);
      digitalWrite(led, LOW);
      delay(OFF_DELAY);
    }
  }

}
