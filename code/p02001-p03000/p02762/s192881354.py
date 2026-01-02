import numpy as np
from collections import defaultdict


class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        """
        x が属するグループを探索
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)

    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]


def main():
    N, M, K = [int(x) for x in input().split()]

    uf = UnionFind(N)
    fcount = defaultdict(int)
    for _ in range(M):
        A, B = [int(x) for x in input().split()]
        uf.union(A-1, B-1)
        fcount[A-1]+=1
        fcount[B-1]+=1

    import collections
    bcount = defaultdict(int)
    for _ in range(K):
        C, D = [int(x) for x in input().split()]
        C-=1
        D-=1
        if uf.is_same(C, D):
            bcount[C]+=1
            bcount[D]+=1

    groups = collections.defaultdict(set)
    for i in range(N):
        groups[uf.find(i)].add(i)

    counts = []
    for i in range(N):
        friends = groups[uf.find(i)]
        cnt = len(friends)-1-fcount[i]-bcount[i]
        counts.append(cnt)
    print(" ".join(map(str, counts)))


if __name__ == '__main__':
    main()