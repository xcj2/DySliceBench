class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parents = [-1] * N

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
        return (i for i in range(self.N) if self.find(i) == root)

    def roots(self):
        return (i for i, x in enumerate(self.parents) if x < 0)

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        dic = {}
        for x in range(self.N):
            r = self.find(x)
            dic.setdefault(r, [])
            dic[r].append(x)
        return dic


import sys
sys.stdin.readline

def main():
    N, K, L = map(int, input().split())
    UF1 = UnionFind(N)
    UF2 = UnionFind(N)
    for _ in range(K):
        p, q = map(int, input().split())
        UF1.union(p-1, q-1)
    for _ in range(L):
        r, s = map(int, input().split())
        UF2.union(r-1, s-1)
    P = [None] * N
    D = {}
    for i in range(N):
        T = (UF1.find(i), UF2.find(i))
        P[i] = T
        D.setdefault(T, 0)
        D[T] += 1
    print(*[D[p] for p in P])


if __name__ == "__main__":
    main()