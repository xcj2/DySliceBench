import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
from math import *
from itertools import *
INF = float('inf')

class SegmentTree:

    def __init__(self, N):
        self.N = 1<<(N-1).bit_length()
        self.data = [None] * (2*self.N)

    def Update(self, l, r, t, v):
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

    def getValue(self, x):
        x += self.N-1
        ret = (-1, INF)
        while x >= 0:
            if self.data[x]:
                ret = max(ret, self.data[x])
            x = (x-1)//2
        return ret[1]

N, Q = map(int, input().split())
stx = [[int(x) for x in input().split()] for i in range(N)]
stx.sort(key = lambda v : -v[2])
D = [(int(input()), i) for i in range(Q)]
D.sort(key = lambda v : v[0])
d, p = [d for d, p in D], [p for d, p in D]
seg = SegmentTree(Q)
for i, (s, t, x) in enumerate(stx):
    l = bisect_left(d, s-x)
    r = bisect_left(d, t-x)
    seg.Update(l, r, i, x)
ans = [None] * Q
for i in range(Q):
    tmp = seg.getValue(i)
    if tmp == INF:
        tmp = -1
    ans[p[i]] = tmp
print(*ans, sep = '\n')
