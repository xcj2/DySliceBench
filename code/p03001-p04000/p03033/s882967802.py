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
        for _ in range(num): return []
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(map(int, input().split())) for _ in range(N)]
        return map(list,zip(*read_all))

#################

from operator import itemgetter
from bisect import bisect_left

N,Q = II()
a = []
for _ in range(N):
    s,t,x = II()
    a.append((x, s-x-0.5, t-x-0.5))
a.sort(key=itemgetter(0))
D = Line(Q,1)

ans = [-1]*(Q+1)
right = [0]*Q
for a0 in a:
    l = bisect_left(D,a0[1])
    r = bisect_left(D,a0[2])
    while l<r:
        while ans[l]!=-1:
            l = right[l]
            if l==N:
                break
        if l>=r:
            break
        ans[l] = a0[0]
        right[l] = r
        l += 1

for i in range(Q):
    print(ans[i])