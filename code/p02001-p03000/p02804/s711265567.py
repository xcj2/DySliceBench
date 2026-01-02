from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())


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
        if n <= 0:
            return 0
        elif n < k:
            return 0
        else:
            return self.fac[n]*self.invmod[k]%mod *self.invmod[n-k] %mod


N,K = inpl()
C = Combination(N)
aa = sorted(inpl())

ans = 0
for i,a in enumerate(aa):
    ans += a * (C.calc(i,K-1) - C.calc(N-i-1,K-1)) %mod
    ans %= mod

print(ans)
