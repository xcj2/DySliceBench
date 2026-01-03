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
        return len(list(self.roots()))

    def all_group_members(self):
        dic = {}
        for x in range(self.N):
            r = self.find(x)
            dic.setdefault(r, [])
            dic[r].append(x)
        return dic

import sys
input=sys.stdin.readline
def main():
    N,M=map(int, input().split())
    L=[list(map(int, input().split()))[1:]for _ in range(N)]
    UF=UnionFind(N+M)
    for i in range(N):
        for l in L[i]:
            UF.union(i,N+l-1)
    b=set(i for i in UF.members(0) if i < N)==set(range(N))
    print("YNEOS"[not b::2])

if __name__ == "__main__":
    main()