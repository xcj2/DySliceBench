import sys

readline = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n
        self.rank = [0]*n
    
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
        
        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
        else:
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

def main():
    n, q = map(int, readline().split())
    uf = UnionFind(n)
    for _ in range(q):
        com, x, y = map(int, readline().split())
        if com == 0:
            uf.union(x, y)
        else:
            px = uf.find(x)
            py = uf.find(y)
            print((px == py)*1)


if __name__ == "__main__":
    main()

