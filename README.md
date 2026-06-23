# Project_LEDBox

Un projet de boîtier à LEDs piloté par un **Seeed Studio XIAO ESP32-C3**, incluant la conception 3D du boîtier, le schéma électronique et deux programmes de séquenceur LED.

---

## Aperçu du montage

> Prototype sur breadboard : XIAO ESP32-C3 + 4 LEDs (blanche, rouge, jaune, verte) avec résistances de protection.

---

## Structure du projet

```
Project_LEDBox/
├── FreeCAD/                  # Modèles 3D du boîtier (fichiers .FCStd)
├── Fritzing plan/            # Schéma électronique du circuit (fichier .fzz)
├── Led_sequencer_DNA/        # Programme ESP32-C3 – séquence à thème ADN
└── Led_sequencer_test/       # Programme ESP32-C3 – tests et validation du câblage
```

---

## Matériel nécessaire

| Composant | Description |
|---|---|
| **Seeed Studio XIAO ESP32-C3** | Microcontrôleur principal (Wi-Fi + BLE, USB-C) |
| **4 LEDs** | Blanche, Rouge, Jaune, Verte (5 mm) |
| **4 résistances** | 1x 0 Ω (LED blanche), 3x 47 Ω (LED rouge, jaune, verte) |
| **Mini breadboard** | Pour le prototypage |
| **Fils de connexion** | Jumper wires |
| **Boîtier imprimé en 3D** | Fichiers fournis dans `FreeCAD/` |

---

## Schéma électronique

Le schéma complet est disponible dans le dossier `Fritzing plan/`. Il peut être ouvert avec [Fritzing](https://fritzing.org/).

Brochage typique sur le XIAO ESP32-C3 :

| LED | Broche XIAO | Résistance |
|---|---|---|
| Blanche | D0 | 0 Ω |
| Rouge | D1 | 47 Ω |
| Jaune | D2 | 47 Ω |
| Verte | D3 | 47 Ω |

- **Cathode (−) de chaque LED** → GND (via résistance)
- **VCC** → 3,3 V (broches 3V3 du XIAO)

> ⚠️ Le XIAO ESP32-C3 fonctionne en **3,3 V logique**. Ne pas connecter directement à du 5 V.

---

## Boîtier 3D

Les fichiers de conception du boîtier sont dans le dossier `FreeCAD/`. Ils peuvent être ouverts et modifiés avec [FreeCAD](https://www.freecad.org/) (open source).

Paramètres d'impression recommandés :
- Matériau : **PLA**
- Épaisseur de couche : **0,2 mm**
- Remplissage : **20 %** minimum

---

## Programmes

### `Led_sequencer_test`

Programme de test pour vérifier le bon fonctionnement du câblage et des LEDs. À utiliser en premier pour valider l'installation.

### `Led_sequencer_DNA`

Programme principal générant une animation lumineuse inspirée de la structure d'une **double hélice d'ADN**. Les LEDs s'allument de manière séquentielle pour reproduire un effet visuel en spirale.

---

## Installation et utilisation

### Prérequis

1. [Arduino IDE](https://www.arduino.cc/en/software) v2.x
2. Ajouter le support **ESP32** dans l'IDE Arduino :
   - `Fichier > Préférences > URL de gestionnaire de cartes supplémentaires` :
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
     ```
   - `Outils > Type de carte > Gestionnaire de cartes` → rechercher **esp32** → Installer
3. Sélectionner la carte : `Outils > Type de carte > ESP32 Arduino > XIAO_ESP32C3`

### Étapes

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Bastien-mnt0/Project_LEDBox.git
   ```
2. Ouvrir le sketch souhaité (`Led_sequencer_DNA/` ou `Led_sequencer_test/`).
3. Vérifier les **numéros de broches** en haut du fichier `.ino` et les adapter si besoin.
4. Brancher le XIAO ESP32-C3 en USB-C.
5. Compiler et téléverser (`Ctrl+U`).
6. Admirer le résultat

---

## Personnalisation

Les paramètres principaux à ajuster dans les sketches :

```cpp
#define LED_BLANC   D0   // Broche LED blanche
#define LED_ROUGE   D1   // Broche LED rouge
#define LED_JAUNE   D2   // Broche LED jaune
#define LED_VERTE   D3   // Broche LED verte
#define DELAY_MS    100  // Vitesse de la séquence (ms)
```

---

## Licence

Ce projet est open source. Libre à vous de l'utiliser, le modifier et le partager.

---

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une *issue* ou une *pull request*.