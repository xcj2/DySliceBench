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
    n, m, k = map(int, input().split())
    friends = [0]*(n+1)
    blocks = [[] for _ in range(n+1)]
    uf = UnionFind(n)
    ans = ""
    for _ in range(m):
        a, b = map(int, input().split())
        friends[a] += 1
        friends[b] += 1
        uf.unite(a, b)
    for _ in range(k):
        c, d = map(int, input().split())
        blocks[c].append(d)
        blocks[d].append(c)
    for i in range(1, n+1):
        nf = friends[i]
        nb = 0
        for b in blocks[i]:
            if uf.same(i, b):
                nb += 1
        ans += "{} ".format(uf.size(i) - 1 - nf - nb)
    print(ans)


if __name__ == "__main__":
    main()