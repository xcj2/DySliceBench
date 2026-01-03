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
    
    def unite(self, x, y):
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
    
    def isSame(self, x, y):
        return self.find(x) == self.find(y)

from collections import defaultdict
def solve():
    N, K, L = map(int, input().split())
    road_uf = UnionFind(N)
    train_uf = UnionFind(N)

    for i in range(K):
        p, q = map(lambda x: int(x)-1, input().split())
        road_uf.unite(p, q)

    for i in range(L):
        r, s = map(lambda x: int(x)-1, input().split())
        train_uf.unite(r, s)

    ma = defaultdict(int)
    for v in range(N):
        root_road = road_uf.find(v)
        root_train = train_uf.find(v)
        ma[str(root_road) + "_" + str(root_train)] += 1
    
    for v in range(N):
        root_road = road_uf.find(v)
        root_train = train_uf.find(v)
        print(ma[str(root_road) + "_" + str(root_train)], end=' ')

if __name__ == '__main__':
    solve()