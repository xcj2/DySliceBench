#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(A: int, B: int, N: int):
    if N < B:
        ret = A * N // B - A * (N // B)
    else:
        a = A * (B - 1) // B
        m = (N // B) * B - 1
        b = A * m // B - A * (m // B)
        c = A * N // B - A * (N // B)
        ret = max(a, b, c)
    print(ret)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(A, B, N)

if __name__ == '__main__':
    main()
