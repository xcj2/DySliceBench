#!/usr/bin/env python3
import sys


def solve(N: int, X: int, L: "List[int]"):
    d = 0
    ret = 1
    for l in L:
        d += l
        if d <= X:
            ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    L = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, X, L)

if __name__ == '__main__':
    main()
