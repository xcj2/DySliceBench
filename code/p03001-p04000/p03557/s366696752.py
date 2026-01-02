#!/usr/bin/env python3
import sys
from bisect import bisect_left
INF = float("inf")


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    A.sort()
    B.sort()
    C.sort()
    count = 0
    for b in B:
        countA = bisect_left(A, b)
        countC = N-bisect_left(C, b+1)
        count += countA*countC
    print(count)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C)


if __name__ == '__main__':
    main()
