# Project_LEDBox

An LED box project controlled by a **Seeed Studio XIAO ESP32-C3**, including 3D enclosure design, electronic schematics, and LED sequencer programs inspired by DNA sequences.

---

## Project Overview

Breadboard prototype: XIAO ESP32-C3 + 4 LEDs (white, red, yellow, green) with protection resistors.

Each LED corresponds to a DNA base:

| LED | Color | DNA Base |
|---|---|---|
| `D0` | Green | G (Guanine) |
| `D1` | Yellow | C (Cytosine) |
| `D2` | Red | A (Adenine) |
| `D3` | Blue/White | T (Thymine) |

---

## Project Structure

```
Project_LEDBox/
├── FreeCAD/
│   ├── V1/                          # V1 enclosure files
│   │   ├── LEDBox-V1.FCStd
│   │   ├── LEDBox.3mf
│   │   ├── LEDBox-BoxLid.3mf
│   │   └── LEDBox-TopOfTheBox.3mf
│   ├── LEDBox.FCStd                 # Current FreeCAD design
│   ├── LEDBox2.3mf                  # Main enclosure (printable)
│   ├── LEDBox-BoxLid2.3mf           # Lid (printable)
│   ├── LEDBox-TopOfTheBox2.3mf      # Top panel (printable)
│   ├── Mini-Breadboard YELLOW.STEP  # Breadboard reference model
│   └── Seeed Studio XIAO-ESP32-C3.step  # XIAO reference model
│
├── Fritzing plan/
│   ├── V1.fzz / V1.png              # V1 schematic
│   ├── V2.fzz / V2.png              # V2 schematic (current)
│   └── seeed-xiao-esp32-tht.fzpz   # XIAO Fritzing part
│
├── Led_sequencer_DNA/
│   ├── Led_sequencer_DNA_1/         # Fixed DNA sequence (GFP gene)
│   │   ├── Led_sequencer_DNA_1.ino
│   │   ├── sequence.fasta           # DNA sequence source
│   │   └── update_dna_sequence.py  # Script to update sequence from FASTA
│   └── Led_sequencer_DNA_2/         # Random sequence selector
│       ├── Led_sequencer_DNA_2.ino
│       ├── sequence.fasta
│       └── update_dna_sequence.py
│
└── Led_sequencer_test/
    └── Led_sequencer_test.ino       # Basic LED test
```

---

## Required Hardware

| Component | Description |
|---|---|
| **Seeed Studio XIAO ESP32-C3** | Main microcontroller (Wi-Fi + BLE, USB-C) |
| **4 LEDs** | Green (D0), Yellow (D1), Red (D2), Blue/White (D3) |
| **4 Resistors** | 1x 10 Ω (white LED), 3x 47 Ω (red, green, yellow LEDs) |
| **4x Heat Set Inserts M3** | [CNC Kitchen M3 Standard](https://cnckitchen.store/products/heat-set-insert-m3-x-5-7-100-pieces) – for enclosure assembly |
| **4x Screws M3x8mm countersunk** | Flat head screws to secure the lid |
| **Mini breadboard** | For prototyping |
| **Jumper wires** | Connection wires |
| **3D-printed enclosure** | Files provided in `FreeCAD/` |

---

## Electronic Schematic

Schematics are available in the `Fritzing plan/` folder (open with [Fritzing](https://fritzing.org/)).
A V1 and V2 version are provided.

Pinout on the XIAO ESP32-C3:

| LED | XIAO Pin | Resistor | DNA Base |
|---|---|---|---|
| Green | D0 | 47 Ω | G |
| Yellow | D1 | 47 Ω | C |
| Red | D2 | 47 Ω | A |
| Blue/White | D3 | 10 Ω | T |

- **Cathode (−) of each LED** → GND (via resistor)
- **VCC** → 3.3 V (XIAO 3V3 pin)

> The XIAO ESP32-C3 operates at **3.3 V logic**. Do not connect directly to 5 V.

---

## 3D Enclosure

Design files are in `FreeCAD/`. Open and edit with [FreeCAD](https://www.freecad.org/) (open source).
Printable `.3mf` files are ready to slice directly.

Two versions are available: **V1** (archived in `FreeCAD/V1/`) and the current **V2**.

Recommended print settings:
- Material: **PLA**
- Layer height: **0.2 mm**
- Infill: **20%** minimum

---

## Programs

### `Led_sequencer_test`

Basic test program: lights each LED up one by one sequentially to verify wiring.

- ON delay: 300 ms
- OFF delay: 150 ms

### `Led_sequencer_DNA_1` — Fixed DNA sequence

Reads a hardcoded DNA sequence (the **GFP gene** — Green Fluorescent Protein) and lights the corresponding LED for each base:

```
A → Red (D2)    T → Blue/White (D3)    G → Green (D0)    C → Yellow (D1)
```

The DNA sequence in the `.ino` can be updated automatically from a `.fasta` file using the provided Python script:

```bash
python3 update_dna_sequence.py
```

Simply replace `sequence.fasta` with any FASTA file and run the script — it will update `Led_sequencer_DNA_1.ino` automatically.

### `Led_sequencer_DNA_2` — Random sequence selector

Same LED-to-base mapping, but picks a sequence **at random** from a list of sequences defined in the `.ino`. After each full sequence, a transition animation (all LEDs blink) plays before the next one starts.

---

## Installation and Usage

### Prerequisites

1. [Arduino IDE](https://www.arduino.cc/en/software) v2.x
2. Add **ESP32** board support:
   - `File > Preferences > Additional Boards Manager URLs`:
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
     ```
   - `Tools > Board > Boards Manager` → search **esp32** → Install
3. Select: `Tools > Board > ESP32 Arduino > XIAO_ESP32C3`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Bastien-mnt0/Project_LEDBox.git
   ```
2. Open the desired sketch in Arduino IDE.
3. Connect the XIAO ESP32-C3 via USB-C.
4. Compile and upload (`Ctrl+U`).

---

## Customization

### Change the DNA sequence (DNA_1)

Replace `sequence.fasta` with any FASTA file, then run:

```bash
python3 update_dna_sequence.py
```

The script will automatically update the `DNA_sequence[]` array in the `.ino` file.

### Timing

Adjust delays at the top of any `.ino` file:

```cpp
const int ON_DELAY  = 300;  // LED on duration (ms)
const int OFF_DELAY = 150;  // LED off duration (ms)
```

### Add sequences (DNA_2)

Edit the `DNA_sequences[]` array in `Led_sequencer_DNA_2.ino`:

```cpp
const char* DNA_sequences[] = {
  "ATGCGT...",
  "TGCACAGG...",
};
```

---

## License

This project is open source. Feel free to use, modify, and share it.

---

## Contributing

Contributions are welcome! Feel free to open an issue or a pull request.
