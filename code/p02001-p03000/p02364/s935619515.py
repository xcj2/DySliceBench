class UnionFind:
    def __init__(self, V):
        self.group = [i for i in range(V)]
        self.rank = [0] * V

    def find(self, x):
        if x != self.group[x]:
            self.group[x] = self.find(self.group[x])
        return self.group[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            self.group[x] = y
        else:
            self.group[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def is_same_group(self, x, y):
        return self.find(x) == self.find(y)

class Edge:
    def __init__(self, FROM, TO, WEIGHT):
        self.FROM = FROM
        self.TO = TO
        self.WEIGHT = WEIGHT

    def __lt__(self, arg):
        return self.WEIGHT < arg.WEIGHT

V, E = map(int, input().split())

UF = UnionFind(V)

G = []
for _ in range(E):
    s, t, w = map(int, input().split())
    G.append(Edge(s, t, w))
G = sorted(G)

ans = 0
for i in range(E):
    if UF.is_same_group(G[i].FROM, G[i].TO):
        continue
    UF.unite(G[i].FROM, G[i].TO)
    ans += G[i].WEIGHT

print(ans)

