class Word:
    def __init__(self, word: str, type: str):
        self.word = word
        self.type = type

class Noun(Word):
    pass

class Adjective(Word):
    pass

class NounPhrase(Word):
    pass

class Verb(Word):
    pass

class VerbPhrase(Word):
    pass

class Preposition(Word):
    pass

class ProperNoun(Word):
    pass


