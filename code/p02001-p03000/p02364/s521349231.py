from heapq import heappush, heappop

class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))

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
            self.parents[y] = x


V, E = map(int, input().split())
q = []
K = {}
ans = 0
S = UnionFind(V)

for _ in range(E):
    s, t, w = map(int, input().split())
    heappush(q, (w, s, t))
#print(q)
# クラスカル法
while len(q) > 0:
    w, s, t = heappop(q)
    if S.find(s) != S.find(t):
        ans += w
        S.union(s,t)
print(ans)
