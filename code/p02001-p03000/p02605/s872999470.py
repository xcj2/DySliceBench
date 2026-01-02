import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
XYU = []
from bisect import bisect_left
from collections import defaultdict
UR = defaultdict(list)
UL = defaultdict(list)
DR = defaultdict(list)
DL = defaultdict(list)
LR = defaultdict(list)
UD = defaultdict(list)
for _ in range(N):
    x, y, u = input().split()
    x, y = int(x), int(y)
    XYU.append((x, y, u))
XYU.sort()
for x, y, u in XYU:
    if u=='U':
        UL[(x-y)].append((x, y))
    if u=='R':
        LR[y].append((x, y))
    if u=='D':
        DL[(x+y)].append((x, y))
    if u=='U':
        UR[(x+y)].append((x, y))
        UD[x].append((x, y))
    if u=='R':
        DR[(x-y)].append((x, y))

ans = 10**18
def check(x, y, u):
    global ans
    if u=='R':
        leng = len(UR[x+y])
        if leng:
            idx = bisect_left(UR[x+y], (x, y, u))
            if idx<leng:
                ans = min(ans, UR[x+y][idx][0]-x)

    if u=='L':
        leng = len(UL[x-y])
        if leng:
            idx = bisect_left(UL[x-y], (x, y, u))
            if idx>0:
                ans = min(ans, x-UL[x-y][idx-1][0])
        
        leng = len(DL[x+y])
        if leng:
            idx = bisect_left(DL[x+y], (x, y, u))
            if idx>0:
                ans = min(ans, x-DL[x+y][idx-1][0])
        
        leng = len(LR[y])
        if leng:
            idx = bisect_left(LR[y], (x, y, u))
            if idx>0:
                ans = min(ans, (x-LR[y][idx-1][0])/2)

    if u=='D':
        leng = len(UD[x])
        if leng:
            idx = bisect_left(UD[x], (x, y, u))
            if idx>0:
                ans = min(ans, (y-UD[x][idx-1][1])/2)

        leng = len(DR[x-y])
        if leng:
            idx = bisect_left(DR[x-y], (x, y, u))
            if idx>0:
                ans = min(ans, x-DR[x-y][idx-1][0])

for x, y, u in XYU:
    check(x, y, u)

if ans>=10**16:
    print('SAFE')
else:
    print(int(ans*10))

