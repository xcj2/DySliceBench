from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().rstrip().split()
def S(): return sys.stdin.readline().rstrip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]

mod=10**9+7

n=I()

fac = [1] * (n + 1)
inv = [1] * (n + 1)
for j in range(1, n + 1):
    fac[j] = fac[j-1] * j % mod

inv[n] = pow(fac[n], mod-2, mod)
for j in range(n-1, -1, -1):
    inv[j] = inv[j+1] * (j+1) % mod


def comb(n, r):
    if r > n or n < 0 or r < 0:
        return 0
    return fac[n] * inv[n - r] * inv[r] % mod



G=[[]for _ in range(n)]
for _ in range(n-1):
    a,b=LI()
    G[a-1]+=[b-1]
    G[b-1] += [a-1]

cnt=[-1]*n
par=[-1]*n
def f(x):
    ret=1
    for y in G[x]:
        if par[x]==y:
            continue
        par[y]=x
        ret+=f(y)
    cnt[x]=ret
    return ret

f(0)
D=[0]*n
def tree_dp(x):
    c = 1
    remain_v = cnt[x] - 1
    for y in G[x]:
        if y == par[x]:
            continue
        c = c * tree_dp(y) * comb(remain_v, cnt[y]) % mod
        remain_v -= cnt[y]
    D[x] = c
    if x: return c

tree_dp(0)
ans=[0]*n
ans[0]=D[0]



q=deque([0])
while q:
    e=q.pop()
    for d in G[e]:
        if d==par[e]:
            continue
        ans[d]=pow(comb(n-1,cnt[d])*D[d],mod-2,mod)*ans[e]*comb(n-1,cnt[d]-1)*D[d]%mod
        q+=[d]

print(*ans,sep="\n")