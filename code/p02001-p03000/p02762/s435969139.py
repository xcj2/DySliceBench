#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):

    conns = [[] for _ in range(N)]
    for i in range(M):
        conns[A[i] - 1].append(B[i] - 1)
        conns[B[i] - 1].append(A[i] - 1)

    par = list(range(N))
    counts = [0] * N
    ret = [0] * N

    def find_root(x):
        if par[x] != x:
            par[x] = find_root(par[x])
        return par[x]

    def is_same_group(a, b):
        a_root = find_root(a)
        b_root = find_root(b)
        return par[a_root] == b_root

    def union(a, b):
        a_root = find_root(a)
        b_root = find_root(b)
        par[a_root] = b_root
        return

    for i in range(M):
        a, b = A[i] - 1, B[i] - 1
        union(a, b)

    for i in range(N):
        root = find_root(i)
        counts[root] += 1

    for i in range(N):
        root = find_root(i)
        ret[i] = counts[root] - len(conns[i]) - 1

    for i in range(K):
        a, b = C[i] - 1, D[i] - 1
        if is_same_group(a, b):
            ret[a] -= 1
            ret[b] -= 1

    print(' '.join([str(r) for r in ret]))
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (K)  # type: "List[int]"
    D = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, M, K, A, B, C, D)

if __name__ == '__main__':
    main()
