#!/usr/bin/env python3
import sys


def solve(S: str):
    n = len(S)
    while True:
        l = len(S)
        i = 0
        while True:
            if i >= len(S) - 1:
                break
            if S[i] != S[i + 1]:
                S = S[:i] + S[i + 2:]
                i = max(i - 1, 0)
            else:
                i += 1
        if l == len(S):
            break
    print(n - len(S))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = str(next(tokens))  # type: int
    solve(S)

if __name__ == '__main__':
    main()
