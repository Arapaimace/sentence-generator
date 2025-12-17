from pathlib import Path

def read(path: Path) -> Sentence:
    with open(path) as file:
        for line in file:
            ...