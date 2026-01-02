#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 2  # type: int


import math
import collections


def solve(N: int, a: "List[int]"):
    b = [0]*N
    for i in range(N-1, -1, -1):
        tmp = 0
        for j in range(2, N//(i+1)+1):
            tmp += b[j*(i+1)-1]
        if tmp % MOD == a[i]:
            b[i] = 0
        else:
            b[i] = 1

    c = [i+1 for i, val in enumerate(b) if val % 2 > 0]
    print(len(c))
    if len(c) != 0:
        print(*c, sep=" ")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
