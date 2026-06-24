# Project_LEDBox

An LED box project controlled by a **Seeed Studio XIAO ESP32-C3**, including the 3D enclosure design, electronic schematic, and two LED sequencer programs.

---

## Project Overview

> Breadboard prototype: XIAO ESP32-C3 + 4 LEDs (white, red, yellow, green) with protection resistors.

---

## Project Structure

```
Project_LEDBox/
├── FreeCAD/                  # 3D enclosure models (.FCStd files)
├── Fritzing plan/            # Circuit schematic (.fzz file)
├── Led_sequencer_DNA/        # ESP32-C3 program – DNA-themed sequence
└── Led_sequencer_test/       # ESP32-C3 program – wiring tests and validation
```

---

## Required Hardware

| Component | Description |
|---|---|
| **Seeed Studio XIAO ESP32-C3** | Main microcontroller (Wi-Fi + BLE, USB-C) |
| **4 LEDs** | White, Red, Yellow, Green (5 mm) |
| **4 Resistors** | 1x 10 Ω (white LED), 3x 47 Ω (red, yellow, green LEDs) |
| **Mini breadboard** | For prototyping |
| **Jumper wires** | Connection wires |
| **3D-printed enclosure** | Files provided in `FreeCAD/` |

---

## Electronic Schematic

The full schematic is available in the `Fritzing plan/` folder. It can be opened with [Fritzing](https://fritzing.org/).

Typical pinout on the XIAO ESP32-C3:

| LED | XIAO Pin | Resistor |
|---|---|---|
| White | D0 | 0 Ω |
| Red | D1 | 47 Ω |
| Yellow | D2 | 47 Ω |
| Green | D3 | 47 Ω |

- **Cathode (−) of each LED** → GND (via resistor)
- **VCC** → 3.3 V (XIAO 3V3 pins)

> The XIAO ESP32-C3 operates at **3.3 V logic**. Do not connect directly to 5 V.

---

## 3D Enclosure

The enclosure design files are in the `FreeCAD/` folder. They can be opened and edited with [FreeCAD](https://www.freecad.org/) (open source).

Recommended print settings:
- Material: **PLA**
- Layer height: **0.2 mm**
- Infill: **20%** minimum

---

## Programs

### `Led_sequencer_test`

Test program to verify that the wiring and LEDs are working correctly. Use this first to validate the setup.

### `Led_sequencer_DNA`

Main program generating a light animation inspired by the structure of a **DNA double helix**. The LEDs light up sequentially to reproduce a spiral visual effect.

---

## Installation and Usage

### Prerequisites

1. [Arduino IDE](https://www.arduino.cc/en/software) v2.x
2. Add **ESP32** support in the Arduino IDE:
   - `File > Preferences > Additional Boards Manager URLs`:
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
     ```
   - `Tools > Board > Boards Manager` → search for **esp32** → Install
3. Select the board: `Tools > Board > ESP32 Arduino > XIAO_ESP32C3`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Bastien-mnt0/Project_LEDBox.git
   ```
2. Open the desired sketch (`Led_sequencer_DNA/` or `Led_sequencer_test/`).
3. Check the **pin numbers** at the top of the `.ino` file and adjust if needed.
4. Connect the XIAO ESP32-C3 via USB-C.
5. Compile and upload (`Ctrl+U`).
6. Enjoy the result!

---

## Customization

Main parameters to adjust in the sketches:

```cpp
#define LED_WHITE   D0   // White LED pin
#define LED_RED     D1   // Red LED pin
#define LED_YELLOW  D2   // Yellow LED pin
#define LED_GREEN   D3   // Green LED pin
#define DELAY_MS    100  // Sequence speed (ms)
```
