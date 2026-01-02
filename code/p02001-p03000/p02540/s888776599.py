import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
idx_dic = {}
XY = []
for i in range(N):
    x, y = mapint()
    x, y = x-1, y-1
    idx_dic[i] = y
    XY.append((x, y))
XY.sort()

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

uf = UnionFind(N)
from heapq import heappush, heappop
Q = []
for i in range(N):
    x, y = XY[i]
    mini = None
    while Q:
        v = heappop(Q)
        if v>y:
            heappush(Q, v)
            break
        uf.union(v, y)
        if mini is None:
            mini = v
    if mini is None:
        heappush(Q, y)
    else:
        heappush(Q, mini)
for i in range(N):
    print(uf.size(idx_dic[i]))
