from grammar import Word
class Rule:
    def __init__(self, result: list[Word], definition):
        self.result = result
        self.definition = definition