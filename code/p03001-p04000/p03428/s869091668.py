MIS = lambda: map(int,input().split())
from math import acos

def ccw(p1, p2, p3):
    # positive -> ccw; negative -> cw; 0 -> collinear
    return (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])

def ConvexHull(p):
    U = []; L = []; p.sort()
    for q in p:
        while len(U)>1 and ccw(U[-2], U[-1], q) >= 0: U.pop()
        while len(L)>1 and ccw(L[-2], L[-1], q) <= 0: L.pop()
        U.append(q); L.append(q)
    return U + L[-2:0:-1]

def angle(v1, v2):
    inner = v1[0]*v2[0] + v1[1]*v2[1]
    v1s = (v1[0]**2 + v1[1]**2) ** .5
    v2s = (v2[0]**2 + v2[1]**2) ** .5
    return acos(inner / v1s / v2s)

n = int(input())
if n == 1: print(1); exit()
if n == 2: print(0.5); print(0.5); exit()

p = [tuple(MIS())+(i,) for i in range(n)]
CH = ConvexHull(p)
bsc = []
for i in range(len(CH)):
    x1, y1, i1 = CH[i]
    x2, y2, i2 = CH[i-1]
    bsc.append((y1-y2, x2-x1))
if len(CH) == 2: angles = [1, 1]
else: angles = [angle(bsc[i], bsc[i-1]) for i in range(len(CH))]
S = sum(angles)

ans = [0] * n
for i in range(len(CH)):
    x, y, ind = CH[i-1]
    ans[ind] = angles[i] / S
for x in ans: print(x)