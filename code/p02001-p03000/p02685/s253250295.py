import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

def fact_all(n,M=mod):
    f = [1]*(n+1)
    ans = 1
    for i in range(1,n+1):
        ans = (ans*i)%M
        f[i] = ans
    return f

## inv(0!)~inv(n!)をmodしつつ求める
def fact_inv_all(fact_all,M=mod):
    N = len(fact_all)
    finv = [0]*N
    finv[-1] = pow(fact_all[-1],M-2,M)
    for i in range(N-1)[::-1]:
        finv[i] = finv[i+1]*(i+1)%M
    return finv

## nCkをmodしつつ返す
def nCk(n,k,fact_list,inv_list,M=mod):
    return (((fact_list[n]*inv_list[k])%M)*inv_list[n-k])%M

N,M,K = LI()

Ma = [0]*(N)
Ma[0] = 1
for i in range(1,len(Ma)):
    Ma[i] = Ma[i-1]*(M-1)
    Ma[i] %= mod

fl = fact_all(N)
il = fact_inv_all(fl)

ans = 0
for j in range(K+1):
    ans += nCk(N-1,j,fl,il)*Ma[N-1-j]*M
    ans %= mod

print(ans)