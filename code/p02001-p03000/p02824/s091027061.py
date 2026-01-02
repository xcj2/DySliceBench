#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, M: int, V: int, P: int, A: "List[int]"):

    # 降順
    A.sort(reverse=True)
    acc = [0]+list(accumulate(A))

    left = P-1
    right = len(A)
    L = M*(V-N)-acc[P-1]
    K = A[P-1]-M
    while right - left > 1:
        mid = (right + left)//2
        cap = (mid-P+1)*A[mid] - acc[mid]
        if A[mid] < K or cap < L:
            right = mid
        else:
            left = mid
    print(right)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    V = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, V, P, A)


if __name__ == '__main__':
    main()
