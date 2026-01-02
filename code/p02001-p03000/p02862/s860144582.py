class combination():
    #素数のmod取るときのみ　速い
    def __init__(self, n, mod):
        self.n = n
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for j in range(1, n + 1):
            self.fac[j] = self.fac[j - 1] * j % mod

        self.inv[n] = pow(self.fac[n], mod - 2, mod)
        for j in range(n - 1, -1, -1):
            self.inv[j] = self.inv[j + 1] * (j + 1) % mod

    def comb(self, n, r, mod):
        if r > n or n < 0 or r < 0:
            return 0
        return self.fac[n] * self.inv[n - r] * self.inv[r] % mod

def examD(mod):
    X, Y = LI()
    if (X+Y)%3!=0:
        ans = 0
    else:
        N = (X+Y)//3
        if N>Y:
            ans = 0
        else:
            k = (N-(X-Y))//2
            C = combination(N,mod)
            ans = C.comb(N,k,mod)
    print(ans)


import sys,copy,bisect,itertools
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD(mod)
