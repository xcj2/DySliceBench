class UnionFind(object):
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1]*size

    def __str__(self):
        from collections import defaultdict
        d = defaultdict(set)
        for i in range(len(self.parent)):
            d[self.find(i)].add(i)
        return str(dict(d))    

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
    N,M = map(int,input().split())
    uf = UnionFind(N)
    p = list(map(lambda x:int(x)-1,input().split()))
    for i in range(M):
        x,y = map(lambda x:int(x)-1,input().split())
        uf.unite(x, y)
    ans = 0
    for i in range(N):
        if uf.same(p[i], i):
            ans += 1
    print(ans)