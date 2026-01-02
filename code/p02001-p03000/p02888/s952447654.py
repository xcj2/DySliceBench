#!/usr/bin/env python3
import sys
INF = float("inf")
from bisect import bisect_left


def solve(N: int, L: "List[int]"):
    # a<=b<=c
    L.sort()
    counter = 0
    for i in range(N-2):
        a = L[i]
        for j in range(i+1, N-1):
            b = L[j]
            k = bisect_left(L[j+1:], a+b)
            counter += k
    print(counter)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L)


if __name__ == '__main__':
    main()
