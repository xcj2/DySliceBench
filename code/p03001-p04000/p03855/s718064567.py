class UnionFind(object):
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1]*size

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.size[y] += self.size[x]
            self.parent[x] = y
        else:
            self.size[x] += self.size[y]
            self.parent[y] = x
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def sizeofset(self, x):
        return self.size[self.find(x)]

if __name__ == "__main__":
    N,K,L = map(int,input().split())
    uf_road = UnionFind(N)
    uf_rail = UnionFind(N)
    for _ in range(K):
        p,q = map(int,input().split())
        p -= 1
        q -= 1
        uf_road.unite(p,q)
    for _ in range(L):
        r,s = map(int,input().split())
        r -= 1
        s -= 1
        uf_rail.unite(r,s)
    roots = [None]*N
    for i in range(N):
        roots[i] = (uf_road.find(i), uf_rail.find(i))
    from collections import defaultdict
    d = defaultdict(int)
    for r in roots:
        d[r] += 1
    print(" ".join([str(d[roots[i]]) for i in range(N)]))
