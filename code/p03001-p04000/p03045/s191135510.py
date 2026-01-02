from collections import defaultdict, deque
def inpl(): return list(map(int, input().split()))

class UnionFind():

    def __init__(self, N):
        self.parent = [-1] * (N+1)
        self.size = [1] * (N+1)

    def find(self, x):
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x_p = self.find(x)
        y_p = self.find(y)
        if x_p != y_p:
            if self.size[x_p] < self.size[y_p]:
                x_p, y_p = y_p, x_p
            self.size[x_p] += self.size[y_p]
            self.parent[y_p] = x_p

N, M = inpl()
UFT = UnionFind(N)

for _ in range(M):
    x, y, z = inpl()
    UFT.unite(x, y)

print(UFT.parent[1:].count(-1))