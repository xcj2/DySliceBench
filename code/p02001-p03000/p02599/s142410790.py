import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
    def sum(self, i):  # 区間 [1, i]の和
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
    def add(self, i, x):  # iにxを加算
        while i <= self.size:
            self.tree[i] += x
            i += i & -i  
    def pos(self, idx):  # idxの値を取得
        return self.sum(idx) - self.sum(idx-1)
    def lower_bound(self, w):  # w以上の値を持つ最小のidxを検索
        if w <= 0:
            return 0
        idx = 0
        k = 1
        while k*2 <= self.size:
            k *= 2
        while k > 0:
            if idx+k <= self.size and self.tree[idx+k] < w:
                w -= self.tree[idx+k]
                idx += k
            k //= 2
        return idx+1

N, Q = MAP()
c = LIST()
ilr = [[i]+LIST() for i, _ in enumerate(range(Q))]
ilr.sort(key=lambda x:x[2])
bit = Bit(N)
rtmp = ilr[0][2]
last = [None]*(N+1)
for i in range(rtmp):
    last[c[i]] = i+1
for i in range(1, N+1):
    if last[i]:
        bit.add(last[i], 1)

ans = [0]*Q
for i, l, r in ilr:
    if rtmp < r:
        for j in range(rtmp+1, r+1):
            if last[c[j-1]]:
                bit.add(last[c[j-1]], -1)
            last[c[j-1]] = j
            bit.add(j, 1)
        rtmp = r
    ans[i] = bit.sum(r)-bit.sum(l-1)

print(*ans, sep="\n")
