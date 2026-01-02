def examA():
    N, R = LI()
    ans = R+100*max(0,(10-N))
    print(ans)
    return

def examB():
    N, K = LI()
    ans = 1
    while(N>=K):
        N //=K
        ans += 1
    print(ans)
    return

def examC():
    N = I()
    X = LI()
    ans = inf
    for i in range(101):
        cur = 0
        for x in X:
            cur += (i-x)**2
        ans = min(ans,cur)
    print(ans)
    return

def examD():
    def cmb(n, r, mod):
        cur = 1
        for i in range(r):
            cur *= (n-i)
            cur %= mod
        for i in range(r):
            cur *= pow(i+1,mod-2,mod)
            cur %= mod
        return cur
    n, a, b = LI()
    ans = pow(2,n,mod) - cmb(n,a,mod) - cmb(n,b,mod) -1
    ans = (ans+mod*2)%mod
    print(ans)
    return

def examE():
    class combination():
        # 素数のmod取るときのみ　速い
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
    n, k = LI()
    C = combination(2*10**5+1,mod)
    if k>n:
        k = n
    ans = 0
    for i in range(k+1):
        cur = C.comb(n,i,mod) * C.comb(n-1,i,mod)
        ans += cur
        ans %= mod
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
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

if __name__ == '__main__':
    examE()

"""

"""