#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')
move = [(0, 1), (1, 1), (-1, 1), (0, -1), (1, -1), (-1, -1), (1, 0), (-1, 0)]
#A
def A():
    a, b, c = LI()
    if a == b:
        print(c)
    if b == c:
        print(a)
    if a == c:
        print(b)
    return

#B
def B():
    h, w = LI()
    s = SR(h)
    for y in range(h):
        for x in range(w):
            if s[y][x] == ".":
                b = 0
                for my, mx in move:
                    ym = my + y
                    xm = mx + x
                    if 0 <= ym < h and 0 <= xm < w:
                        if s[ym][xm] == "#":
                            b += 1
                s[y][x] = b
    for i in range(h):
        print("".join(map(str, s[i])))
    return

#C
def C():
    n, m = LI()
    edg = [[] for i in range(n)]
    ab = LIR_(m)
    for a,b in ab:
        edg[a].append(b)
        edg[b].append(a)
    ans = 0
    for a, b in ab:
        c = [True] * n
        ed = defaultdict(int)
        q = deque()
        q.append(0)
        c[0] = False
        ed[(a,b)] = True
        while q:
            now = q.pop()
            for e in edg[now]:
                if ed[(now,e)] or ed[(e,now)]:
                    continue
                ed[(now, e)] = True
                c[e] = False
                q.appendleft(e)
        if True in c:
            ans += 1
    print(ans)
    return

#D
def D():
    n, k = LI()
    xy = LIR(n)
    fullserch = list(itertools.combinations(range(n), 2))
    ans = inf
    for a, b in fullserch:
        minx = min(xy[a][0], xy[b][0])
        maxx = max(xy[a][0], xy[b][0])
        for c, d in fullserch:
            miny = min(xy[c][1], xy[d][1])
            maxy = max(xy[c][1], xy[d][1])
            x = 0
            
            for i in range(n):
                if minx <= xy[i][0] <= maxx and miny <= xy[i][1] <= maxy:
                    x += 1

            if x >= k:
                ans = min(ans, (maxx - minx) * (maxy - miny))
    print(ans) 
    return

#Solve
if __name__ == '__main__':
    D()
