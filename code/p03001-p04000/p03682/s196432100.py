from heapq import heappop, heappush

class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x,y = y,x
            self.parents[y] = x
            self.size[x] += self.size[y]

N = int(input())
x = [None] * N
y = [None] * N
for i in range(N):
    a, b = map(int, input().split())
    x[i] = (a,i)
    y[i] = (b,i)

x.sort()
y.sort()
q = []
for i in range(N-1):
    heappush(q, (abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]))
    heappush(q, (abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]))

uf = UnionFind(N)
ans = 0
# クラスカル法
while len(q) > 0:
    w, s, t = heappop(q)
    if uf.find(s) != uf.find(t):
        ans += w
        uf.union(s,t)
print(ans)