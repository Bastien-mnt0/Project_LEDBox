const int redled    = D0;
const int blueled   = D1;
const int greenled  = D2;
const int yellowled = D3;

const int NB_LEDS = 4;
const int leds[]  = { redled, blueled, greenled, yellowled };

const int ON_DELAY  = 300;
const int OFF_DELAY = 150;

const char DNA_sequence[] = "ATGCGTACCTGATCGTAGCTAGGCTAACGTTGACCTAGCGTATCGGATCCGTAAGCTTGCATGCGTACGATCGTTAACGCGATGCTAGCTAGCATGGCCTA";

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < NB_LEDS; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }

  Serial.println("Séquenceur ADN prêt.");
  Serial.print("Longueur de la séquence : ");
  Serial.println(strlen(DNA_sequence));
}

void loop() {
  for (int i = 0; i < (int)strlen(DNA_sequence); i++) {

    char base = DNA_sequence[i];
    int  led  = -1;

    switch (base) {
      case 'A': led = redled;    Serial.print("A → Rouge  "); break;
      case 'T': led = blueled;   Serial.print("T → Bleu   "); break;
      case 'G': led = greenled;  Serial.print("G → Vert   "); break;
      case 'C': led = yellowled; Serial.print("C → Jaune  "); break;
      default:
        Serial.print("? → ignoré");
        break;
    }

    Serial.println(base);

    if (led != -1) {
      digitalWrite(led, HIGH);
      delay(ON_DELAY);
      digitalWrite(led, LOW);
      delay(OFF_DELAY);
    }
  }

  Serial.println("--- Fin de séquence, redémarrage ---");
  delay(1000);
}
