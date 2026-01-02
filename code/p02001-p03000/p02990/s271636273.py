from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

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
        if n < 0 or k < 0 or n < k:
            return 0
        elif n == 0 or k == 0 or n == k:
            return 1
        return self.fac[n]*self.invmod[k]%mod *self.invmod[n-k] %mod

N,K = inpl()
a = K
b = N-K
Com = Combination(2010)

for i in range(1,K+1):
    ans = 0
    an = i
    # A, ABA, ABABA,,,
    bn = i-1
    if bn == 0 and b==0:
        ans += 1
    else:
        ans += Com.calc(a-1,(an-1)) * Com.calc(b-1,(bn-1))
    #print(a,an,b,bn)
    #print(Com.calc(a-1,(an-1)) * Com.calc(b-1,(bn-1)))

    # AB(BA)
    bn = i
    ans += Com.calc(a-1,(an-1)) * Com.calc(b-1,(bn-1))*2
    #print(a,an,b,bn)
    #print(Com.calc(a-1,(an-1)) * Com.calc(b-1,(bn-1))*2)

    # BAB
    bn = i+1
    ans += Com.calc(a-1,(an-1)) * Com.calc(b-1,(bn-1))
    #print(a,an,b,bn)
    #print(Com.calc(a-1,(an-1)) * Com.calc(b-1,(bn-1)))

    print(ans%mod)
    #print()
