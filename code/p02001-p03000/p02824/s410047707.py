#!/usr/bin/env python3
import sys
from bisect import bisect_left, bisect_right
INF = float("inf")


def solve(N: int, M: int, V: int, P: int, A: "List[int]"):

    A.sort()

    # 二分探索で探す
    left = -1
    right = len(A)-1
    while right - left > 1:
        mid = (right + left)//2

        if N-P <= mid:
            right = mid
            continue

        if A[mid]+M < A[N-P]:
            left = mid
            continue

        # 入れられても構わない票をカウントする
        tot = 0
        for i in range(mid+1, N-P+1):
            tot += A[mid]+M-A[i]
        tot += (P-1)*M
        tot += mid*M
        tot += M

        if tot < M*V:
            left = mid
            continue
        else:
            right = mid
            continue

    print(N-bisect_left(A, A[right]))
    # Yがわかったときの答え

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
