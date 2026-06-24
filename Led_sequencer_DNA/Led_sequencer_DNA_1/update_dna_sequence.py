import re
import sys
from pathlib import Path

# Folder where this script is located
BASE_DIR = Path(__file__).parent

FASTA_FILE = BASE_DIR / "sequence.fasta"
INO_FILE   = BASE_DIR / "Led_sequencer_DNA_1.ino"

# --- Read the sequence from the FASTA file ---
sequence = ""
with open(FASTA_FILE, "r") as f:
    for line in f:
        if not line.startswith(">"):       # ignore the header line
            sequence += line.strip().upper()  # concatenate and uppercase

print(f"Sequence read: {len(sequence)} bases")

# --- Split into 70-base chunks ---
CHUNK = 70
chunks = [sequence[i:i+CHUNK] for i in range(0, len(sequence), CHUNK)]
formatted = "\n".join(f'  "{chunk}"' for chunk in chunks)
replacement = f"const char DNA_sequence[] =\n{formatted};"

# --- Replace the DNA_sequence declaration in the .ino ---
with open(INO_FILE, "r") as f:
    content = f.read()

new_content = re.sub(
    r'const char DNA_sequence\[\]\s*=\s*(?:"[^"]*"\s*)+;',
    replacement,
    content,
    flags=re.DOTALL
)

if new_content == content:
    print("ERROR: DNA_sequence[] line not found in the .ino file")
    sys.exit(1)

with open(INO_FILE, "w") as f:
    f.write(new_content)

print(f"'{INO_FILE}' updated successfully.")