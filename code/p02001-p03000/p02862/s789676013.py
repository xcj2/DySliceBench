from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

ans = 0
[x,y] = inpl()

alpha = ( 2*x-y )//3
beta = (2*y-x)//3
alpha_c = ( 2*x-y )%3
beta_c = (2*y-x)%3

MAX_NUM = 10**6 + 1
MOD = 10**9+7

fac  = [0]*MAX_NUM
finv = [0]*MAX_NUM
inv  = [0]*MAX_NUM

fac[0]  = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1

for i in range(2,alpha+beta+1):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def combinations(n,k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD

ans = combinations(alpha+beta,alpha) if alpha_c == 0 and beta_c == 0 else 0
print(ans)