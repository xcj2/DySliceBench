#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    ab = sorted(zip(A, B))
    k = 0
    ans = 0
    for Ai, Bi in ab:
        v = min(M - k, Bi)
        k += v
        ans += Ai * v
        if k >= M:
            break
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)


if __name__ == '__main__':
    main()
