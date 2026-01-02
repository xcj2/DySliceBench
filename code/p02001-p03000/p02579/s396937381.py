#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def S(): return input().rstrip()
def LS(): return S().split()
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float("INF")

#solve
def solve():
    h, w = LI()
    ch, cw = LI_()
    dh, dw = LI_()
    q = deque()
    s = [None] * h
    c = [None] * h
    for i in range(h):
        s[i] = S()
        c[i] = [inf] * w
    q.append((ch, cw))
    c[ch][cw] = 0
    while q:
        nh, nw = q.popleft()
        now = c[nh][nw]
        for mh, mw in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            mh += nh
            mw += nw
            if 0 <= mh < h and 0 <= mw < w and c[mh][mw] > now and s[mh][mw] == ".":
                c[mh][mw] = now
                q.appendleft((mh, mw))
        for i in range(-2, 3):
            i += nh
            for j in range(-2, 3):
                j += nw
                if 0 <= i < h and 0 <= j < w and c[i][j] > now + 1 and s[i][j] == ".":
                    c[i][j] = now + 1
                    q.append((i, j))
    print(-1 if c[dh][dw] == inf else c[dh][dw])
    return


#main
if __name__ == '__main__':
    solve()
