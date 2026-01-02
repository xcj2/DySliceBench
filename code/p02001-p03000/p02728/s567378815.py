class treedp_rerooting():
    def __init__(self, N, V, MOD):
        self.N = N
        self.V = V
        self.mod = MOD
        self.rep = [0] * N
        self.children = [-1] * N
        self.A = [0] * N
        self.C = combination(N, MOD)
        return

    # 子の数のカウント
    def dfs(self, s):
        size = 1
        nowchild = []
        cur = 1
        self.children[s] = 0
        for i in self.V[s]:
            if self.children[i] != -1:
                continue
            ns, nc = self.dfs(i)
            nowchild.append(ns)
            size += ns
            cur *= nc
            cur %= self.mod
        self.children[s] = size
        rest = size - 1
        for k in nowchild:
            cur *= self.C.comb(rest, k)
            rest -= k
            cur %= self.mod
        self.A[s] = cur
        return size, cur

    def dfs2(self, s, p=-1):
        cur = 1
        rest = self.N - 1
        for to in self.V[s]:
            cur *= self.A[to]
            cur %= self.mod
        for to in self.V[s]:
            cur *= self.C.comb(rest, self.children[to])
            rest -= self.children[to]
            cur %= self.mod
        self.rep[s] = cur

        n = len(self.V[s])
        L = [0] * n; R = [0] * n
        L2 = [0] * n; R2 = [0] * n

        for i, ne in enumerate(self.V[s]):
            L[i] = R[i] = self.A[ne] * self.C.inv[self.children[ne]] % self.mod
            L2[i] = R2[i] = self.children[ne]
        for i in range(1, n):
            L[i] *= L[i - 1]
            L[i] %= self.mod
            L2[i] += L2[i - 1]
        for i in range(1, n - 1)[::-1]:
            R[i] *= R[i + 1]
            R[i] %= self.mod
            R2[i] += R2[i + 1]
        for i, ne in enumerate(self.V[s]):
            if ne == p:
                continue
            self.A[s] = 1
            self.children[s] = 1
            if i > 0:
                self.A[s] *= L[i - 1]
                self.A[s] %= self.mod
                self.children[s] += L2[i - 1]
            if i + 1 < n:
                self.A[s] *= R[i + 1]
                self.A[s] %= self.mod
                self.children[s] += R2[i + 1]
            self.A[s] *= self.C.fac[self.N - self.children[ne] - 1]
            self.A[s] %= self.mod
            self.dfs2(ne, s)
        return

class combination():
    # 素数のmod取るときのみ　速い
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for j in range(1, n + 1):
            self.fac[j] = self.fac[j - 1] * j % mod

        self.inv[n] = pow(self.fac[n], mod - 2, mod)
        for j in range(n - 1, -1, -1):
            self.inv[j] = self.inv[j + 1] * (j + 1) % mod

    def comb(self, n, r):
        if r > n or n < 0 or r < 0:
            return 0
        return self.fac[n] * self.inv[n - r] * self.inv[r] % self.mod

def ABC160():
    N = I()
    V = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = LI()
        a -= 1; b -= 1
        V[a].append(b)
        V[b].append(a)
    dp_r = treedp_rerooting(N,V,mod)
    dp_r.dfs(0)
    dp_r.dfs2(0)

    ans = dp_r.rep

    for v in ans:
        print(v)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque

def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    ABC160()

"""
8
1 2
2 3
3 4
3 5
3 6
6 7
6 8
"""

# 40
# 280
# 840
# 120
# 120
# 504
# 72
# 72

