#!/usr/bin/env python3
import json, sys, re

# Load the translation dictionary
with open("translation.json", "r", encoding="utf-8") as f:
    vocab = json.load(f)

def translate_line(line):
    for word, symbol in vocab.items():
        if re.search(rf"\b{word}\b", line, re.IGNORECASE):
            return f"{symbol} : {line.strip()}"
    return line.strip()

def translate_file(filename):
    print(f"\n--- {filename} ---")
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(translate_line(line))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./translate-reminders.py REMINDERS-XXX.md")
        sys.exit(1)
    for file in sys.argv[1:]:
        translate_file(file)

