from heapq import *

class UnionFind:
    def __init__(self, n):
        '木の初期化をする'
        self.p = [-1] * n
        self.rank = [1]*n
    def find(self, x):
        'x の親を返す'
        if self.p[x] == -1:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        'rankの低い親を高い方のの親にする'
        if not self.same(x,y):
            x = self.find(x)
            y = self.find(y)
            if self.rank[x] > self.rank[y]:
                x,y = y,x
            elif self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.p[x] = y
            return True
        else:
            return False

    def same(self, x, y):
        return self.find(x) == self.find(y)

n,m = map(int,input().split())
a = list(map(int,input().split()))
uf = UnionFind(n)
ans = 0
for i in range(m):
    x,y = map(int,input().split())
    uf.unite(x, y)
if n < 2*(n-m-1):
    print('Impossible')
    exit(0)
if m == n-1:
    print(0)
    exit(0)
tree = {}
pq = []
heapify(pq)
for i in range(n):
    p = uf.find(i)
    if not p in tree.keys():
        ans += a[i]
        tree[p] = a[i]
    else:
        if tree[p] <= a[i]:
            heappush(pq, a[i])
        else:
            ans += a[i] - tree[p]
            heappush(pq, tree[p])
            tree[p] = a[i]
l = len(tree)

for _ in range(2*(n-m-1) - l):
    ans += heappop(pq)
print(ans)
