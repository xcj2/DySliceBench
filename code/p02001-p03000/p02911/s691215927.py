#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(N: int, K: int, Q: int, A: "List[int]"):
    c = Counter(A)
    for i in range(1, N+1):
        if K-(Q-c[i]) > 0:
            yes()
        else:
            no()
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, K, Q, A)


if __name__ == '__main__':
    main()
