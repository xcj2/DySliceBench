#!/usr/bin/env python3
import sys


def solve(N: int, M: int, X: int, A: "List[int]"):
    l, r = 0, 0
    for a in A:
        if a < X:
            l += 1
        else:
            r += 1
    ret = min(l, r)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(M) ]  # type: "List[int]"
    solve(N, M, X, A)

if __name__ == '__main__':
    main()
