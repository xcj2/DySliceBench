import sys
input = sys.stdin.readline


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

    def union(self, x, y):
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    H, W = map(int, input().split())
    S = []
    for h in range(H):
        S.append(input().strip())

    uf = UnionFind(H*W)
    for i in range(H):
        for j in range(W):
            if i < H-1 and S[i][j] != S[i+1][j]:
                uf.union(i*W+j, (i+1)*W+j)
            if j < W-1 and S[i][j] != S[i][j+1]:
                uf.union(i*W+j, i*W+(j+1))
    D = {}
    for i in range(H):
        for j in range(W):
            r = uf.find(i*W+j)
            if r not in D:
                D[r] = [0, 0]
            if S[i][j] == "#":
                D[r][0] += 1
            else:
                D[r][1] += 1
    ans = 0
    for d in D.values():
        ans += d[0]*d[1]
    print(ans)


if __name__ == '__main__':
    main()
