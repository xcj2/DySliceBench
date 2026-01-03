from collections import defaultdict
import heapq

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def getParent(self):
        return [self.find(i) for i in range(N)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if (root_x == root_y):
            return
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        elif self.rank[root_y] > self.rank[root_x]:
            self.parent[root_x] = root_y

        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    def memsInGroup(self, x):
        """
        O(N)かかります
        """
        root = self.find(x)
        return [i for i in range(N) if root == self.find(i)]

    def sizeOfGroup(self, x):
        return len(self.memsInGroup(x))

class Edge:

    def __init__(self, u, v, cost):
        self.u = u
        self.v = v
        self.cost = cost

N = int(input())
vertex = {}
for i in range(N):
    x, y = map(int, input().split())
    vertex[i] = (x, y)

sortX = sorted(vertex.items(), key=lambda x:x[1][0])
sortY = sorted(vertex.items(), key=lambda x:x[1][1])

edges = []

for i in range(N-1):
    v1 = sortX[i]
    v2 = sortX[i+1]
    edges.append(Edge(v1[0]-1, v2[0]-1, abs(v1[1][0] - v2[1][0])))

for i in range(N-1):
    v1 = sortY[i]
    v2 = sortY[i+1]
    edges.append( Edge(v1[0]-1, v2[0]-1, abs(v1[1][1] - v2[1][1]) ) )

edges.sort(key = lambda x: x.cost)
uf = UnionFind(N)

res = 0
for e in edges:
    if not uf.isSame(e.u, e.v):
        uf.unite(e.u, e.v)
        res += e.cost

print(res)
