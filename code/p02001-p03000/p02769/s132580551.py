from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N,K = inpl()

def comb(N,x):
    ret = 1
    for i in range(N-x+1,N+1):
        ret *= i
        ret %= mod

    for i in range(1, x+1):
        ret *= pow(i,mod-2,mod)
        ret %= mod

    return ret%mod

class Combination:
    def __init__(self,N):
        self.fac = [1]*(N+1)
        for i in range(1,N+1):
            self.fac[i] = (self.fac[i-1]*i)%mod
        self.invmod = [1]*(N+1)
        self.invmod[N] = pow(self.fac[N],mod-2,mod)
        for i in range(N,0,-1):
            self.invmod[i-1] = (self.invmod[i]*i)%mod

    def calc(self,n,k):#nCk
        return self.fac[n]*self.invmod[k]%mod *self.invmod[n-k] %mod




if N <= K:
    ans = comb(N*2-1, N)
    print(ans)
else:
    C = Combination(200000+3)
    ans = 0
    for z in range(K+1):
        r = N - z
        m = N - r
        ans += C.calc(N, z) * C.calc(r+m-1, m)
        ans %= mod

    print(ans)
