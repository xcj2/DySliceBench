import sys
input = sys.stdin.buffer.readline

class UnionFind:
    __slots__ = ["data"]
    
    def __init__(self, n=0):
        self.data = [-1]*(n+1)
    
    def root(self, x):
        if self.data[x] < 0:
            return x
        self.data[x] = self.root(self.data[x])
        return self.data[x]
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.data[x] < self.data[y]:
                self.data[x] += self.data[y]
                self.data[y] = x
            else:
                self.data[y] += self.data[x]
                self.data[x] = y
    
    def same(self, x, y):
        return self.root(x) == self.root(y)
    
    def size(self, x):
        return -self.data[self.root(x)]


def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    uf = UnionFind(n)
    for _ in range(m):
        x, y = map(int, input().split())
        uf.unite(x, y)
    cnt = 0
    for i in range(1, n+1):
        if uf.same(i, p[i-1]):
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()