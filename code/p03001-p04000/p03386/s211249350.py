#!/usr/bin/env python3
import sys


def solve(A: int, B: int, K: int):
    s = set()
    for i in range(A, min(A + K, B + 1)):
        s.add(i)
    for i in range(max(B - K + 1, A + K - 1), B + 1):
        s.add(i)
    ret = sorted(list(s))
    for n in ret:
        print(n)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(A, B, K)

if __name__ == '__main__':
    main()
