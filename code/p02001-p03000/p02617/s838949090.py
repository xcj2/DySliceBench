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

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if not directed:
            pt[t[i]-1].append(s[i]-1)
    return pt

N = I()
u,v = LIR(N-1,2)

pt = edges_to_pt(u,v,N)
ans = 0
d = 0
for i in range(N):
    s = 0
    for v in pt[i]:
        if v < i:
            s += v+1
    d = d-s+i+1
    ans += d

print(ans)