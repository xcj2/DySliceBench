from itertools import combinations
from math import ceil
N = int(input())
A = list(map(int, input().split()))
M = ceil(N*(N+1)/4)

class FenwickTree(object):
    def __init__(self, n):
        self._bit = [0] * (n+1)
        self.n = n+1
    
    def add(self, i, a):
        i += 1
        while i < self.n:
            self._bit[i] += a
            i += i & -i
    
    def sum(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self._bit[i]
            i -= i & -i
        return ret

lo, hi = 0, max(A)+1
while lo < hi-1:
    mid = (lo+hi)//2
    B = [1 if a >= mid else -1 for a in A]
    C = []
    C.append(0)
    for b in B:
        C.append(C[-1]+b)
    cmin = min(C)
    for i in range(N+1):
        C[i] -= cmin  # offset
    cmax = max(C)+1
    fw = FenwickTree(cmax)
    cnt = 0
    for i in range(N+1):
        cnt += fw.sum(C[i])
        fw.add(C[i], 1)

    if cnt >= M:
        lo = mid
    else:
        hi = mid

print(lo)
