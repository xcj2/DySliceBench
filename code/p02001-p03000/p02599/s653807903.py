import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
C = list(map(int,input().split()))
LR = [tuple(map(int,input().split())) for i in range(Q)]

qs = [[] for _ in range(N)]
for i,(l,r) in enumerate(LR):
    qs[l-1].append((i,r-1))

from collections import defaultdict
hist = defaultdict(lambda: -1)
nx = [-1] * N
for i in range(N-1,-1,-1):
    nx[i] = hist[C[i]]
    hist[C[i]] = i

class BinaryIndexedTree:
    def __init__(self,size):
        self.N = size
        self.bit = [0]*(size+1)
    def add(self,x,w): # 0-indexed
        x += 1
        while x <= self.N:
            self.bit[x] += w
            x += (x & -x)
    def _sum(self,x): # 1-indexed
        ret = 0
        while x > 0:
            ret += self.bit[x]
            x -= (x & -x)
        return ret
    def sum(self,l,r): # [l,r)
        return self._sum(r) - self._sum(l)
    def __str__(self): # for debug
        arr = [self.sum(i,i+1) for i in range(self.N)]
        return str(arr)
bit = BinaryIndexedTree(N)

ans = [None] * Q
for l in range(N-1,-1,-1):
    if nx[l] != -1:
        bit.add(nx[l], -1)
    for i,r in qs[l]:
        ans[i] = r-l+1 + bit.sum(l,r+1)

print(*ans, sep='\n')