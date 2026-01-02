#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

YES = "YES"  # type: str
NO = "NO"  # type: str

def solve(A: int, V: int, B: int, W: int, T: int):
    d = abs(A - B)
    if V > W and d / (V - W) <= T:
        ret = YES
    else:
        ret = NO
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    V = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    solve(A, V, B, W, T)

if __name__ == '__main__':
    main()
