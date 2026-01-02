from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
        
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

#初期化
# uf = UnionFind(n)
h,w = inpl()
s = [input() for _ in range(h)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
uf = UnionFind(h*w+5)
def ind(i,j): return i*w+j
for y in range(h):
    for x in range(w):
        for dy,dx in d:
            ny = y+dy
            nx = x+dx
            if 0 <= ny < h and 0 <= nx < w and s[ny][nx] != s[y][x]:
                uf.union(ind(y,x), ind(ny,nx))
# print(uf.parents)f
res = 0
cnt = [[0,0] for _ in range(h*w)]
for i in range(h*w):
    ind = uf.find(i)
    color = 0 if s[i//w][i%w] == '.' else 1
    cnt[ind][color] += 1
for i in range(h*w):
    res += cnt[i][0] * cnt[i][1]
print(res)