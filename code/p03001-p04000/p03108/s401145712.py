from itertools import groupby
 
class UnionFind:
 
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
 
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if self.rank[root_x] < self.rank[root_y]:
            self.parents[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parents[root_y] = root_x
            self.size[root_x] += self.size[root_y]
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[x] += 1
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
 
    def get_size(self, x):
        return self.size[self.find(x)]
 
    def get_group(self):
        arr = sorted([(self.find(node), node) for node in range(self.n)])
        groups = []
        for _, g in groupby(arr, key=lambda x: x[0]):
            groups.append([u[1] for u in g])
        return groups

    
N, M = map(int, input().split())
bridges = []
for _ in range(M):
    bridges.append(list(map(lambda x: int(x)-1, input().split())))
U = UnionFind(N)
F = [N * (N-1) // 2]
for i in range(M-1):
    if not U.is_same(*bridges[M-i-1]):
        F.append(F[i] - U.get_size(bridges[M-i-1][0]) * U.get_size(bridges[M-i-1][1]))
        U.union(*bridges[M-i-1])
    else:
        F.append(F[i])
F.reverse()
for f in F:
    print(f)