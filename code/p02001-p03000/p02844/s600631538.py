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
S = str(input())
d = defaultdict(list)

for i in range(N):
    d[S[i]].append(i)

ans = 0
for i in range(1000):
    now = str(i).zfill(3)
    p = 0
    flag = True
    for j in now:
        p1 = bisect_left(d[j],p)
        if p1>=len(d[j]):
            flag = False
            break
        p = d[j][p1]+1
    if flag:
        ans += 1

print(ans)