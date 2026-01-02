import sys
import math
import numpy as np
import copy


class unionfind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.groupnum = n

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb:
            return
        if(self.rank[pa] < self.rank[pb]):
            self.parent[pa] = pb
        else:
            self.parent[pb] = pa
            if self.rank[pa] == self.rank[pb]:
                self.rank[pa] += 1
        self.groupnum -= 1

    def same(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        return pa == pb

    def find(self, a):
        if self.parent[a] == a:
            return a
        p = self.find(self.parent[a])
        self.parent[a] = p
        return p
    


def main():
    n, m = map(int, input().split())
    edges = [[] for i in range(n)]

    edge_list = []

    for i in range(m):
        a, b = map(int, input().split())
        a, b = a-1, b-1
        edges[a].append(b)
        edges[b].append(a)
        edge_list.append((a, b))

    cnt = 0
    # 除外する辺ごとに。
    for i in range(m):
        uf = unionfind(n)
        for j in range(m):
            if i == j:
                continue
            uf.unite(edge_list[j][0], edge_list[j][1])
        if uf.groupnum >= 2:
            cnt += 1


    print(cnt)
    return 0

if __name__ == '__main__':
    sys.exit(main())