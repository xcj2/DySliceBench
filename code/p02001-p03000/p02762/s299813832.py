def main():
    N, M, K=map(int, input().split())
    friend_or_block = [0 for _ in range(N)]
    friends_chain = UnionFindTree(N)

    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        friends_chain.unite(a, b)
        friend_or_block[a] += 1
        friend_or_block[b] += 1

    for _ in range(K):
        c, d = map(int, input().split())
        c, d = c-1, d-1
        if friends_chain.same(c, d):
            friend_or_block[c] += 1
            friend_or_block[d] += 1

    print(' '.join(map(str, [friends_chain.count(i) - friend_or_block[i] - 1 for i in range(N)])))

class UnionFindTree:
    def __init__(self, n):
        self.parent = [-1 for _ in range(n)]

    def root(self, x):
        p, seq = self.parent[x], list()
        while p >= 0:
            seq.append(x)
            x, p = p, self.parent[p]
        for c in seq: self.parent[c] = x
        return x

    def same(self, x, y): return self.root(x) == self.root(y)

    def count(self, x): return -self.parent[self.root(x)]

    def unite(self, x, y):
        xr, yr = self.root(x), self.root(y)
        if xr == yr: return
        if self.parent[xr] > self.parent[yr]: xr, yr = yr, xr
        self.parent[xr] += self.parent[yr]
        self.parent[yr] = xr

if __name__ == '__main__':
    main()

