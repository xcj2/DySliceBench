#!/usr/bin/env python3
import sys


def solve(N: int, T: int, A: int, H: "List[int]"):
    mn = float('inf')
    ret = -1
    for i in range(N):
        t = T - H[i] * 0.006
        diff = abs(A - t)
        if diff < mn:
            ret = i + 1
            mn = diff
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    H = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, T, A, H)

if __name__ == '__main__':
    main()
