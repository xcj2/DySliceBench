#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: int, B: int, X: "List[int]"):
    ret = 0
    cur = X[0]
    for i in range(1, N):
        ret += min(A * (X[i] - X[i - 1]), B)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    X = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, A, B, X)

if __name__ == '__main__':
    main()
