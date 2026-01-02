import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

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

# nCk
## 0!~n!をmodしつつ求める
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

K = I()
S = list(input())
N = len(S)

fl = fact_all(N+K+1)
il = fact_inv_all(fl)

beki25 = [1]*(N+K+1)
for i in range(1,N+K+1):
    beki25[i] = beki25[i-1]*25
    beki25[i] %= mod

beki26 = [1]*(N+K+1)
for i in range(1,N+K+1):
    beki26[i] = beki26[i-1]*26
    beki26[i] %= mod

ans = 0
for i in range(N-1,N+K):
    ans += nCk(i,N-1,fl,il)*beki25[i-N+1]*beki26[N+K-1-i]
    ans %= mod

print(ans)