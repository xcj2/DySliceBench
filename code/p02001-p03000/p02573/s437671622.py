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
    N,M = map(int,input().split())
    uf = UnionFind(N)
    for _ in range(M):
        a,b = map(int,input().split())
        a -= 1
        b -= 1

        uf.unite(a,b)
    
    ans = 0
    for i in range(N):
        ans = max(ans,uf.size(i))
    
    print(ans)
        
if __name__ == '__main__':
    solve()
