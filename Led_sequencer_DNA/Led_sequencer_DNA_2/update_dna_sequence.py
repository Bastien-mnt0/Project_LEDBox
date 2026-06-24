import re
import sys
from pathlib import Path

# Folder where this script is located
BASE_DIR = Path(__file__).parent

FASTA_FILE = BASE_DIR / "sequence.fasta"
INO_FILE   = BASE_DIR / "Led_sequencer_DNA_2.ino"

# --- Read the sequence from the FASTA file ---
sequence = ""
with open(FASTA_FILE, "r") as f:
    for line in f:
        if not line.startswith(">"):
            sequence += line.strip().upper()

print(f"Sequence read: {len(sequence)} bases")

# --- Split into distinct 70-base chunks ---
CHUNK = 70
chunks = [sequence[i:i+CHUNK] for i in range(0, len(sequence), CHUNK)]
nb_seq = len(chunks)

print(f"Split into {nb_seq} sequences of ~{CHUNK} bases")

# --- Format DNA_sequences[] : one string per entry ---
entries = "\n".join(f'  "{chunk}",' for chunk in chunks)
dna_block = f"const char* DNA_sequences[] = {{\n{entries}\n}};"

# --- Format NB_SEQ ---
nb_seq_line = f"const int NB_SEQ = {nb_seq};"

# --- Read the .ino file ---
with open(INO_FILE, "r") as f:
    content = f.read()

# --- Replace DNA_sequences[] block ---
new_content = re.sub(
    r'const char\* DNA_sequences\[\]\s*=\s*\{.*?\};',
    dna_block,
    content,
    flags=re.DOTALL
)

if new_content == content:
    print("ERROR: DNA_sequences[] block not found in the .ino file")
    sys.exit(1)

# --- Replace NB_SEQ ---
new_content = re.sub(
    r'const int NB_SEQ\s*=\s*\d+;',
    nb_seq_line,
    new_content
)

# --- Write back ---
with open(INO_FILE, "w") as f:
    f.write(new_content)

print(f"'{INO_FILE}' updated successfully ({nb_seq} sequences).")