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

W,H = LI()
p = LIR(W,1)
q = LIR(H,1)

p.sort()
cusum = [p[0]]
for i in range(1,W):
    cusum.append(cusum[-1]+p[i])
ans = cusum[-1]

for i in range(H):
    place = bisect_left(p,q[i])
    temp = cusum[place-1] if place >= 1 else 0
    ans += temp + q[i]*(W+1-place)

print(ans)