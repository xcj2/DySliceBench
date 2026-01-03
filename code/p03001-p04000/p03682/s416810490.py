class UnionFindTree():

    def __init__(self, n):
        #木全体の要素数
        self.n  = n
        #root[x]<0ならそのノードが根でありその値が木の要素数
        self.root = [-1] * (n+1)
        #ランク
        self.rank = [1] * (n+1)

    def find_root(self,x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self,x,y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def is_same(self,x,y):
        return self.find_root(x) == self.find_root(y)

    def count_node(self,x):
        return -1 * self.root[self.find_root(x)]
from heapq import heapify, heappop

n = int(input())

loc = []
for i in range(n):
    x, y = map(int, input().split())
    loc.append((i , x, y))

sort_x = sorted(loc, key=lambda x:x[1])
sort_y = sorted(loc, key=lambda x:x[2])

diff = []

for i in range(n-1):
    diff.append((sort_x[i+1][1]-sort_x[i][1],sort_x[i][0],sort_x[i+1][0]))
    diff.append((sort_y[i+1][2]-sort_y[i][2],sort_y[i][0],sort_y[i+1][0]))

#最小のものから順番に並べる
heapify(diff)

uft = UnionFindTree(n)

ans = 0
while diff:
    w, s, t = heappop(diff)
    if not uft.is_same(s,t):
        uft.unite(s,t)
        ans += w

print(ans)