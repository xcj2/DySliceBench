from collections import defaultdict
class UnionFind:
    def __init__(self,nodes):
        self.parents = {node : node for node in nodes}
    def root(self,x):
        if x == self.parents[x]:
            return x
        else:
            rt = self.root(self.parents[x])
            self.parents[x] = rt
            return rt
    def find(self,x,y):
        return self.root(x) == self.root(y)
    def union(self,x,y):
        self.parents[self.root(x)] = self.root(y)
    def get_sets(self):
        res = defaultdict(list)
        for node, parent in self.parents.items():
            res[self.root(node)].append(node)
        # return [*res.values()]
        return list(res.values())

N,M = map(int,input().split(' '))
p = list(map(int,input().split(' ')))

uf = UnionFind(range(1,N+1))

for i in [0]*M:
    x, y = map(int,input().split(' '))
    uf.union(x,y)

ans = 0
for n in range(1,N+1):
    if uf.find(n,p[n-1]):
        ans += 1
print(ans)



