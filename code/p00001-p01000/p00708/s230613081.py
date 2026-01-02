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

while 1:
    N = int(input())
    if N == 0:
        exit()
    q = []
    ans = 0
    S = UnionFind(N)
    x = [None] * N
    y = [None] * N
    z = [None] * N
    r = [None] * N

    for i in range(N):
        x[i], y[i], z[i], r[i] = map(float, input().split())

    for i in range(N):
        for j in range(i+1, N):
            d = (x[i]-x[j])**2 + (y[i]-y[j])**2 + (z[i]-z[j])**2
            d = d**0.5 - r[i] - r[j]
            heappush(q, (max(0,d), i, j))
    # クラスカル法
    while len(q) > 0:
        d, a, b = heappop(q)
        if S.find(a) != S.find(b):
            ans += d
            S.union(a, b)
    print('{:.3f}'.format(ans))
