#!/usr/bin/env python3
import sys
from collections import Counter
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(N: int, A: "List[int]"):
    c = Counter(A)
    each = [c[key]*(c[key]-1)//2 for key in c]
    # print(c)
    # print(each)
    tot = sum(each)

    for i in range(N):
        print(tot - (c[A[i]]-1))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
