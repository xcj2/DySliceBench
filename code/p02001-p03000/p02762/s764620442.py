import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


class UnionFind:
    # Reference: https://note.nkmk.me/python-union-find/
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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


def main():
    N, M, K = map(int, readline().split())
    AB = [tuple(int(s) - 1 for s in readline().split()) for _ in range(M)]
    CD = [tuple(int(s) - 1 for s in readline().split()) for _ in range(K)]

    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)

    H = [[] for _ in range(N)]
    for c, d in CD:
        H[c].append(d)
        H[d].append(c)

    uf = UnionFind(N)
    for a, b in AB:
        uf.union(a, b)

    ans = [0] * N
    for i in range(N):
        ans[i] = uf.size(i) - len(G[i]) - 1
        for j in H[i]:
            if uf.same(i, j):
                ans[i] -= 1

    print(' '.join(map(str, ans)))
    return


if __name__ == '__main__':
    main()
