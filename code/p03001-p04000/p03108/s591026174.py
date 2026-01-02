from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    #根を返す
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

#初期化
# uf = Unionfind(n)
n,m = inpl()
ab = [inpl() for i in range(m)][::-1]
uf = UnionFind(n)
res = [n*(n-1)//2]
if m == 1:
    print(*res)
    quit()
cnt = 0
for a,b in ab[:m-1]:
    cnt += 1
    na = uf.size(a-1)
    nb = uf.size(b-1)
    uf.union(a-1,b-1)
    ns = uf.size(b-1)
    if na + nb == ns:
        tt = res[-1] - (na*nb)
    else:
        tt = res[-1]
    # if ns == n:
    #     tt = 0
    res.append(tt)

for i in res[::-1]:
    print(i)
       
    