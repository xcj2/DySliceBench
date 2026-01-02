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
    ans = 0
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
    examD()

"""

"""