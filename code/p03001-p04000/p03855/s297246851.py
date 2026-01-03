#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

class UnionFindTree:

    def __init__(self, N):
        self.par = list(range(N))

    def find_root(self, x):
        if self.par[x] != x:
            self.par[x] = self.find_root(self.par[x])
        return self.par[x]

    def union(self, a, b):
        a_root = self.find_root(a)
        b_root = self.find_root(b)
        self.par[a_root] = b_root
        return


def solve(N: int, K: int, L: int, p: "List[int]", q: "List[int]", r: "List[int]", s: "List[int]"):
    k_uf = UnionFindTree(N)
    l_uf = UnionFindTree(N)
    ret = [1] * N
    for i in range(K):
        k_uf.union(p[i] - 1, q[i] - 1)
    for i in range(L):
        l_uf.union(r[i] - 1, s[i] - 1)

    pars = []
    for i in range(N):
        pars.append((k_uf.find_root(i), l_uf.find_root(i), i))
    pars.sort()
    #print(pars)
    ret = [1] * N
    tmp = set()
    for i in range(1, N):
        if pars[i][0] == pars[i - 1][0] and pars[i][1] == pars[i - 1][1]:
            tmp.add(pars[i][2])
            tmp.add(pars[i - 1][2])
        else:
            cnt = len(tmp)
            for x in tmp:
                ret[x] = cnt
            tmp = set()
    for x in tmp:
        ret[x] = len(tmp)
    print(' '.join([str(r) for r in ret]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    p = [int()] * (K)  # type: "List[int]" 
    q = [int()] * (K)  # type: "List[int]" 
    for i in range(K):
        p[i] = int(next(tokens))
        q[i] = int(next(tokens))
    r = [int()] * (L)  # type: "List[int]" 
    s = [int()] * (L)  # type: "List[int]" 
    for i in range(L):
        r[i] = int(next(tokens))
        s[i] = int(next(tokens))
    solve(N, K, L, p, q, r, s)

if __name__ == '__main__':
    main()
