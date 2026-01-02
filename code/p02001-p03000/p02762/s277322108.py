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

def solve():
    N, M, K = map(int, input().split())
    dame = [set() for i in range(N)]
    uf = UnionFind(N)

    for i in range(M):
        a, b = map(lambda x: int(x)-1, input().split())
        
        dame[a].add(b)
        dame[b].add(a)
        uf.unite(a,b)
    
    for i in range(K):
        c, d = map(lambda x: int(x)-1, input().split())
        if not uf.isSame(c, d):
            continue
        dame[c].add(d)
        dame[d].add(c)
    
    ans = []
    for i in range(N):
        mem = uf.size(i) - 1
        mem -= len(dame[i])
        ans.append(mem)
    
    print(*ans, sep=' ')

if __name__ == '__main__':
    solve()