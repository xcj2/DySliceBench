def examA():
    N = I()
    S = [""]*N; T = [""]*N
    for i in range(N):
        S[i],T[i] = LSI()
        T[i] = int(T[i])
    X = SI()
    ans = 0
    flag = False
    for i in range(N):
        if flag:
            ans +=T[i]
        if S[i]==X:
            flag = True
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
    N = I()
    X = LI()
    B = [1]*N
    for i in range(1,N-1):
        B[i+1] =B[i]*(i+1)
        B[i+1] %= mod
    XL = [X[i+1]-X[i] for i in range(N-1)]
    C = combination(N, mod)
    """
        cumL = [0]*N
    cumL[1] = XL[0]
    for i in range(1,N):
        cumL[i+1] = cumL[i]+XL[i]
    print(cumL)
    """
    ans = 0; cur = B[-1]
    now = 0
#    print(B,XL)
    for i in range(N-1):
        ans += cur*XL[i]
        ans %=mod
#        print(ans)
    for i in range(1,N-1):
        now += C.comb(N-1,1+i,mod)
        ans += now*XL[i]
        ans %=mod
#        print(ans)
    print(ans)
    return
"""
4
1 3 6 7
"""
def examB2():
    N = I()
    X = LI()
    L = [0]*(N-1)
    for i in range(N-1):
        L[i] = X[i+1] - X[i]

    S = [1]*N
    for i in range(1,N):
        S[i] = S[i-1] + pow(i+1,mod-2,mod)
    C = combination(N,mod)
    cnt = 0
    for i in range(N-1):
        #print(S[i], L[i], C.fac[N - 1])
        cnt += S[i]*L[i]*C.fac[N-1]%mod
        cnt %= mod
    ans = cnt
    print(ans)
    return

def examC():

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
    examB2()
