#!/usr/bin/env python3
import sys
from collections import deque
sys.setrecursionlimit(1000000)

class UnionFind:
    def __init__(self, num):
        self.par = list(range(1,num+1))
        self.size = [1]*num
    
    def root(self, n):
        if self.par[n-1] != n:
            self.par[n-1] = self.root(self.par[n-1])
        return self.par[n-1]

    def unite(self, a, b):
        a=self.root(a)
        b=self.root(b)
        if a!=b:
            self.par[b-1]=a
            self.size[a-1] += self.size[b-1]
        return
    
    def get_size(self, n):
        return self.size[self.root(n)-1]


def solve(N: int, M: int, K: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):

    fris = [0]*N
    blos = [0]*N

    union = UnionFind(N)
    for ai, bi in zip(A, B):
        union.unite(ai,bi)
        fris[ai-1]+=1
        fris[bi-1]+=1
    
    for ci, di in zip(C, D):
        if union.root(ci) == union.root(di):
            blos[ci-1]+=1
            blos[di-1]+=1
    
    ans = [0]*N
    for i in range(1,N+1):
        s = union.get_size(i)
        s -= fris[i-1]
        s -= blos[i-1]
        s -= 1
        ans[i-1] = s

    print(*ans)
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
