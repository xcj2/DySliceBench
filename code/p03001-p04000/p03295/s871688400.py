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
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

from bisect import bisect_right

N,M = II()

a = []
b = []
for i in range(M):
    a0,b0 = II()
    a.append([a0-1,i])
    b.append([b0-2,i])

a.sort(key=lambda x:x[0])
b.sort(key=lambda x:x[0])
left = [a[i][0] for i in range(M)]
used = [False]*M

ans = 0
pb = 0
for r in b:
    if used[r[1]] == False:
        p = bisect_right(left,r[0])
        for i in range(pb,min(M,p)):
            used[a[i][1]] = True
        pb = p
        ans += 1
    else:
        continue

print(ans)