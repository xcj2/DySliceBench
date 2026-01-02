class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
        
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))
        
        self.n = len(labels)
        self.parents = [-1] * self.n
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}
    
    def find_label(self, x):
        return self.d_inv[super().find(self.d[x])]
    
    def union(self, x, y):
        super().union(self.d[x], self.d[y])
    
    def size(self, x):
        return super().size(self.d[x])
    
    def same(self, x, y):
        return super().same(self.d[x], self.d[y])
    
    def members(self, x):
        root = self.find(self.d[x])
        return [self.d_inv[i] for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [self.d_inv[i] for i, x in enumerate(self.parents) if x < 0]

def main():
    N, M = map(int, input().split())
    l = []
    for _ in range(M):
        a, b = map(int, input().split())
        l.append((a-1, b-1))
    t = N * (N - 1) // 2
    f = [t]
    s = 0
    uf = UnionFind(N)
    for a, b in l[::-1]:
        if not uf.same(a, b):
            s += uf.size(a) * uf.size(b)
        if t - s < 0:
            break
        f.append(t - s)
        uf.union(a, b)
    f.extend([0] * M)
    for i in reversed(f[:M]):
        print(i)
main()
