def examA():
    N = SI()
    ans = 0
    for i in N:
        ans += int(i)
    if ans==1:
        ans = 10
    print(ans)
    return

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
def examB():
    N, A, B, K = LI()
    C = combination(N, mod2)
    Da = []
    for i in range(N+1):
        if (K-A*i)%B!=0 or (K-A*i)//B>N:
            continue
        Da.append((i, (K-A*i)//B))
#    print(Da)
    ans = 0
    for a,b in Da:
        cur = C.comb(N,a,mod2)*C.comb(N,b,mod2)
        ans +=cur
        ans %=mod2
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examB()
