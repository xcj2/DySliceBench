import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

from bisect import bisect_left

N = I()
a = III()

d = defaultdict(list)
for i in range(N):
    d[a[i]].append(i)

now = 0
ans = N
for i in range(1,N+1):
    p = bisect_left(d[i], now)
    if p<=len(d[i])-1:
        now = d[i][p]
        ans -= 1
    else:
        if i==1:
            print(-1)
            exit()
        break

print(ans)