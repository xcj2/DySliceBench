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

# "どこかの連続したK個が同じ色"が必要十分

N,K = LI()
a = LI()

dp_l = [0]*N
for i in range(N):
    if a[i] > 0:
        dp_l[i] = dp_l[i-1] + a[i]
    else:
        dp_l[i] = dp_l[i-1]

dp_r = [0]*N
dp_r[N-1] = a[i] if a[i] > 0 else 0
for i in range(N-1)[::-1]:
    if a[i] > 0:
        dp_r[i] = dp_r[i+1] + a[i]
    else:
        dp_r[i] = dp_r[i+1]

kblacks = [0]*(N-K+1)
kblacks[0] = sum(a[:K])
for i in range(1,N-K+1):
    kblacks[i] = kblacks[i-1]+a[K+i-1]-a[i-1]

ans = -float('inf')
for i in range(N-K+1):
    temp = 0
    if i-1 >= 0:
        temp += dp_l[i-1]
    if i+K <= N-1:  
        temp += dp_r[i+K]
    ans = max(ans,temp,temp+kblacks[i])

print(ans)