#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(S: str, T: str, A: int, B: int, U: str):
    if S == U:
        A -= 1
    if T == U:
        B -= 1
    print(A, B)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    U = next(tokens)  # type: str
    solve(S, T, A, B, U)

if __name__ == '__main__':
    main()
