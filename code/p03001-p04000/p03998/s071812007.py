#!/usr/bin/env python3
import sys


def solve(S_A: str, S_B: str, S_C: str):
    hands = {
        'a': S_A,
        'b': S_B,
        'c': S_C,
    }
    turn = 'a'
    while True:
        if hands[turn] == "":
            print(turn.upper())
            return
        s = hands[turn]
        hands[turn] = s[1:]
        turn = s[0]


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S_A = next(tokens)  # type: str
    S_B = next(tokens)  # type: str
    S_C = next(tokens)  # type: str
    solve(S_A, S_B, S_C)


if __name__ == '__main__':
    main()
