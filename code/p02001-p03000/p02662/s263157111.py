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

N,S = LI()
A = LI()

beki = [1]*(N+1)
for i in range(1,N+1):
    beki[i] = beki[i-1]*2
    beki[i] %= mod

inv2 = pow(2,mod-2,mod)

d = [0]*(S+1)
d[0] = beki[N]

ans = 0
for i in range(N):
    if 0 <= S-A[i] <= S:
        ans += d[S-A[i]]*inv2
        ans %= mod
    diff = [0]*(S+1)
    for k in range(S-A[i]+1):
        diff[k+A[i]] = d[k]*inv2
    for k in range(S+1):
        d[k] += diff[k]
        d[k] %= mod

print(ans)