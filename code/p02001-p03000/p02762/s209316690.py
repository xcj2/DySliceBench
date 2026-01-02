import sys
input = sys.stdin.buffer.readline

class UnionFind:
    __slots__ = ["num", "data"]
    
    def __init__(self, n=0):
        self.num = n
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
    
    def sizes(self):
        return [-self.data[self.root(i)] for i in range(self.num+1)]
                


def main():
    n, m, k = map(int, input().split())
    fb = [0]*(n+1)
    uf = UnionFind(n)
    for _ in range(m):
        a, b = map(int, input().split())
        fb[a] += 1
        fb[b] += 1
        uf.unite(a, b)
    for _ in range(k):
        c, d = map(int, input().split())
        if uf.same(c, d):
            fb[c] += 1
            fb[d] += 1
    size = uf.sizes()
    ans = [size[i]-1-fb[i] for i in range(1, n+1)]
    print(" ".join(list(map(str, ans))))


if __name__ == "__main__":
    main()