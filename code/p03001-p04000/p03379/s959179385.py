#!/usr/bin/env python3
import sys


def solve(N: int, X: "List[int]"):
    x = sorted(X)
    l = x[N // 2 - 1]
    r = x[N // 2]
    for a in X:
        if a <= l:
            print(r)
        else:
            print(l)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, X)

if __name__ == '__main__':
    main()
