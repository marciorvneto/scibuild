from dataclasses import dataclass
import re

enum_count = 0
def iota(reset = False):
    global enum_count
    if reset:
        enum_count = 0
    value = enum_count
    enum_count += 1
    return value

# Token types

PAPER_KW = iota()
EXPERIMENT_KW= iota()
LET_KW = iota()

FOR_KW= iota()
PARFOR_KW = iota()

LEFT_PAR = iota()
RIGHT_PAR = iota()
LEFT_CB = iota()
RIGHT_CB = iota()
LEFT_BR = iota()
RIGHT_BR = iota()
COMMA = iota()

ID = iota()
EQUALS = iota()

STRING = iota()
NUMBER = iota()

WHITESPACE = iota()
COMMENT = iota()

EOF = iota()

# Definitions

TOKEN_DEFINITIONS = [
    [WHITESPACE, "^\s+"],
    [WHITESPACE, "^\/\/[^\r?\n]+\r?\n"],

    [PAPER_KW, "^paper"],
    [EXPERIMENT_KW, "^experiment"],
    [LET_KW, "^let"],

    [LEFT_PAR, "^\("],
    [RIGHT_PAR, "^\)"],
    [LEFT_CB, "^\{"],
    [RIGHT_CB, "^\}"],
    [LEFT_BR, "^\["],
    [RIGHT_BR, "^\]"],
    [COMMA, "^,"],

    [ID, "^[a-zA-Z_][a-zA-Z_\d]*"],
    [EQUALS, "^\="],

    [STRING, "^\"[^\"]*\""],
    [NUMBER, "^[+-]?([0-9]+\.?[0-9]*|\.[0-9]+)"],
]
# Tokenizer

@dataclass
class Token:
    type: int
    value: str

class Tokenizer:
    def __init__(self, text: str):
        self.text = text
        self.cursor = 0
    def get_next_token(self):
        while True:
            if self.cursor >= len(self.text):
                return Token(EOF, "")
            matched = self.match()
            if matched:
                return matched
        raise Exception("Something went wrong")
    def get_all_tokens(self):
        self.cursor = 0
        matches = []
        while self.cursor < len(self.text):
            matches.append(self.get_next_token())
        self.cursor = 0
        return matches
    def match(self):
        for token_type, regex in TOKEN_DEFINITIONS:
            substr = self.text[self.cursor:]
            match = re.search(regex, substr)
            if not match:
                continue
            content = match.group(0)
            self.cursor += len(content)
            if token_type == WHITESPACE:
                return None
            return Token(token_type, content)
        raise Exception(f"Could not match token at position {self.cursor}: \"{self.text[self.cursor]}\"")

