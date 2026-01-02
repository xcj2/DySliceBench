class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n + 1)]
        self.sizes = [1] * (n + 1)
 
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if y < x:
            x, y = y, x
        self.parents[y] = x
        self.sizes[x] += self.sizes[y]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def size(self, x):
        return self.sizes[self.find(x)]

def main():
    n, m, k = map(int, input().split())
    uf = UnionFind(n)
    friends = [0] * n
    blocks = [0] * n
    for i in range(m):
        a, b = map(int, input().split())
        friends[a - 1] += 1
        friends[b - 1] += 1
        uf.unite(a - 1, b - 1)
    for i in range(k):
        c, d = map(int, input().split())
        if uf.same(c - 1, d - 1):
            blocks[c - 1] += 1
            blocks[d - 1] += 1
    ans = [0] * n
    for i in range(n):
        ans[i] = uf.size(i) - friends[i] - blocks[i] - 1
    print(*ans)      

if __name__ == '__main__':
  main()