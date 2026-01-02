#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


sys.setrecursionlimit(1000000)


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    uf = list(range(N))
    n = [1] * N

    def getpar(a: int):
        if a == uf[a]:
            return a
        uf[a] = getpar(uf[a])
        return uf[a]

    def union(a: int, b: int):
        pa = getpar(a)
        pb = getpar(b)
        if pa == pb:
            return 0, 0
        ra = n[pa]
        rb = n[pb]
        n[pa] += n[pb]
        uf[pb] = uf[pa]
        return ra, rb

    k = N * (N - 1) // 2
    ans = []
    A.reverse()
    B.reverse()
    for Ai, Bi in zip(A, B):
        Ai -= 1
        Bi -= 1
        ra, rb = union(Ai, Bi)
        ans.append(k)
        k -= ra * rb

    assert k == 0, k
    for ansi in reversed(ans):
        print(ansi)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)


if __name__ == '__main__':
    main()
