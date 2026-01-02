import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
import functools
import itertools
import math
INF = float('inf')
# MOD = 10**9+7
MOD = 998244353

class SegmentTree:

    def __init__(self, N):
        self.N = 1<<(N-1).bit_length()
        self.data = [None] * (2*self.N)

    # 時刻 t に [l, r) を v に変更する
    def update(self, l, r, t, v):
        L, R, val = l+self.N, r+self.N, (t, v)
        while L < R:
            if R & 1:
                R -= 1
                self.data[R-1] = val
            if L & 1:
                self.data[L-1] = val
                L += 1
            L >>= 1
            R >>= 1

    # 現在の x の値を得る
    def getValue(self, x):
        x += self.N-1
        ret = (-1, INF)
        while x >= 0:
            if self.data[x]:
                ret = max(ret, self.data[x])
            x = (x-1)//2
        return ret[1]

N, M = map(int, input().split())
es = defaultdict(list)
for i in range(M):
    l, r, c = map(int, input().split())
    es[l-1].append((c, r))
if 0 not in es:
    print(-1)
    exit()
for l in es:
    es[l].sort()
seg = SegmentTree(N)
seg.update(0, 1, 0, 0)
seg.update(1, N, 1, INF)
Time = 2
for l in range(N):
    esl = es[l]
    d = seg.getValue(l)
    for c, r in esl:
        s, t = l, r
        while s+1 < t:
            m = (s+t)//2
            if seg.getValue(m) <= d+c:
                s = m
            else:
                t = m
        seg.update(t, r, Time, d+c)
        Time += 1
ans = seg.getValue(N-1)
if ans == INF:
    print(-1)
else:
    print(ans)

