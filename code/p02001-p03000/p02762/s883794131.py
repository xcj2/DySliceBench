class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
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


def main():
    N, M, K = list(map(int, input().split()))
    U = UnionFind(N)
    FR = [0] * N
    for _ in range(M):
        a, b = map(int, input().split())
        U.union(a - 1, b - 1)
        FR[a - 1] += 1
        FR[b - 1] += 1
    r = [0] * N
    LS = {}
    for i in range(N):
        t = U.find(i)
        if t not in LS:
            LS[t] = set()
        LS[t].add(i)
        r[i] = -U.parents[t] - 1 - FR[i]
    for _ in range(K):
        c, d = map(int, input().split())
        c, d = c - 1, d - 1
        if d in LS[U.find(c)]:
            r[c] -= 1
            r[d] -= 1
    print(' '.join(str(i) for i in r))

main()
