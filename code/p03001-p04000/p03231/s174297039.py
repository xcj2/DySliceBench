def examA():
    def gcd(x, y):
        if y == 0:
            return x
        while (y != 0):
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)
    N, M = LI()
    S = SI()
    T = SI()
    L = lcm(N,M)
    for i in range(N):
        if i*M%N!=0:
            continue
        cur = i*M//N
        #print(i,cur)
        if S[i]!=T[cur]:
            L = -1
            break
    print(L)
    return

def examB():
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
    N = I()
    A = LI()
    C = combination(N,mod)
    ans = 0
    cnt = 0
    for i in range(N):
        cnt += C.fac[N]*pow(i+1,mod-2,mod)
        cnt %= mod
        #print(cnt)
    #print(cnt)
    ans += cnt*A[0]
    for i in range(1,N):
        cnt = cnt + C.fac[N]*pow(i+1,mod-2,mod) - C.fac[N]*pow(N-i+1,mod-2,mod)
        cnt += mod
        cnt %= mod
        a = A[i]
        ans += cnt*a
        ans %= mod
        #print(cnt)
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examA()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""