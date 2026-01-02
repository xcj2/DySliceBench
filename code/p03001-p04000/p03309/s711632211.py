#!/usr/bin/env python3
import sys
import math
import itertools
INF = float("inf")


def solve(N: int, A: "List[int]"):
    A = [a-i-1 for i, a in enumerate(A)]
    A.sort()
    s = sum(A)-N*A[0]
    for i in range(len(A)):
        if i == 0:
            continue
        buf = (2*i+1-N-1)*(A[i]-A[i-1])
        if buf <= 0:
            s += buf
        else:
            break
    print(s)
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
