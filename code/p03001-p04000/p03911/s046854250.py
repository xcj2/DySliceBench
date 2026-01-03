n, m = [int(item) for item in input().split()]
query = []
appeared = set()
for i in range(n):
    line = [int(item) for item in input().split()]
    appeared.update(line[1:])
    query.append(line[1:])
    
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

uf = UnionFind(m)
for q in query:
    if len(q) == 1:
        continue
    for item in q[1:]:
        if not uf.same_check(q[0]-1, item-1):
            uf.union(q[0]-1, item-1)
    
par = uf.find(appeared.pop() - 1)
for item in appeared:
    if uf.find(item - 1) != par:
        print("NO")
        exit()
print("YES")