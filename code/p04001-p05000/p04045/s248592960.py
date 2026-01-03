#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(N: int, K: int, D: "List[int]"):

    D = set([str(c) for c in D])
    for ans in range(N, 10*N):
        if set(str(ans)).isdisjoint(D):
            print(ans)
            return

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    D = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, K, D)


if __name__ == '__main__':
    main()
