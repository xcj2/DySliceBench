
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

mod = 10**9+7

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

X,Y = inpl()
X,Y = min(X,Y), max(X,Y)

A = X
B = Y - X

A -= B

if A < 0 or A%3 != 0:
    print(0)
else:
    C = Combination(10**6+10)
    a = A//3
    b = A//3 + B
    print(C.calc(a+b,a))
