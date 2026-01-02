from collections import defaultdict


class UnionFind(object):
    def __init__(self, n):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}
        self.size = {i: 1 for i in range(n)}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y

        else:
            self.parent[y] = x

            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

        self.size[x] += self.size[y]
        self.size[y] = self.size[x]


    def get_size(self, x):
        return self.size[self.find(x)]


n, m, k = map(int, input().split())
As, Bs = list(), list()
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    As.append(a)
    Bs.append(b)

edge_friends = defaultdict(list)
for a, b in zip(As, Bs):
    edge_friends[a].append(b)
    edge_friends[b].append(a)

edge_block = defaultdict(list)
for i in range(k):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    edge_block[c].append(d)
    edge_block[d].append(c)

union_find = UnionFind(n)
for a, b in zip(As, Bs):
    union_find.union(a, b)

counts = list()
for i in range(n):
    parent = union_find.find(i)
    n_blocks = 0
    for node in edge_block[i]:
        if parent == union_find.find(node):
            n_blocks += 1
    n_friends = 0
    for node in edge_friends[i]:
        if parent == union_find.find(node):
            n_friends += 1

    count = union_find.get_size(i) - 1 - n_blocks - n_friends
    counts.append(count)

print(*counts)
