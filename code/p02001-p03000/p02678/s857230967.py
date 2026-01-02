#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)

YES = "Yes"  # type: str

def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    conns = [[] for _ in range(N)]
    for i in range(M):
        conns[A[i] - 1].append(B[i] - 1)
        conns[B[i] - 1].append(A[i] - 1)

    q = [0]
    ret = [-1] * N
    visited = [False] * N
    visited[0] = True
    while True:
        nex = []
        for i in q:
            for con in conns[i]:
                if not visited[con]:
                    nex.append(con)
                    ret[con] = i
                    visited[con] = True
        if len(nex) == 0:
            break
        q = nex
    for r in ret[1:]:
        if r < 0:
            print('No')
            return
    print('Yes')
    for r in ret[1:]:
        print(r + 1)
    return

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
