#!/usr/bin/env python3
# Daydream
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str

tokens = ['dream', 'dreamer', 'erase', 'eraser']

def solve(S: str):
    print(YES if is_valid2(S) else NO)
    return

def is_valid(S):
    if S == '':
        return True
    for token in tokens:
        sub = S[-len(token):]
        if sub == token:
            return is_valid(S[:-len(token)])
    return False

def is_valid2(S):
    import re
    x = r"^(dream|dreamer|erase|eraser)*$"
    return True if re.match(x, S) else False

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
