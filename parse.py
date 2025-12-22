from pathlib import Path
from grammar import Word, Sentence

def read(path: Path) -> Sentence:
    output = []
    with open(path) as file:
        for line in file:
            word, part = line.split(',')
            output.append(Word(word, part))