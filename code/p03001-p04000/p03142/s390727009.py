#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    par = [[] for _ in range(N)]
    chi = [[] for _ in range(N)]
    root = None
    for i in range(N + M - 1):
        chi[A[i] - 1].append(B[i] - 1)
        par[B[i] - 1].append(A[i] - 1)

    #print(chi)
    #print(par)
    for i in range(N):
        if len(par[i]) < 1:
            root = i
            par[i].append(-1)
            break

    cur = {root}
    while len(cur) > 0:
        #print(cur)
        nex = set()
        for idx in cur:
            for c in chi[idx]:
                if len(par[c]) < 2:
                    nex.add(c)
                else:
                    par[c].remove(idx)
        cur = nex

    for i in range(N):
        ret = par[i][0]
        print(ret + 1)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (N-1+M)  # type: "List[int]" 
    B = [int()] * (N-1+M)  # type: "List[int]" 
    for i in range(N-1+M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
