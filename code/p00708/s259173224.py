from math import sqrt
import heapq
# -*- coding: utf-8 *-
# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


class UnionFind:
    """
    sizeによる実装
    """

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1 for _ in range(N)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]

    def same(self, x, y):
        return self.find(x) == self.find(y)


def calc_dist(s1, s2):
    dist = sqrt(sum([abs(a-b)**2 for a, b in zip(s1[:-1], s2[:-1])]))
    return max(dist-s1[3] - s2[3], 0)


def solve():
    N = int(input())
    if N == 0:
        exit()
    spheres = [list(map(float, input().split())) for _ in range(N)]
    dists = []
    Un = UnionFind(N)
    for i in range(N):
        for j in range(i+1, N):
            tmp = calc_dist(spheres[i], spheres[j])
            #dists.append([tmp, i, j])
            heapq.heappush(dists, [tmp, i, j])

    cost = 0
    #dists = sorted(dists, key=lambda x: x[0])
    for k in range(len(dists)):
        dist, i, j = heapq.heappop(dists)
        if Un.same(i, j):
            continue
        else:
            Un.union(i, j)
            cost += dist
    print("{:.3f}".format(cost))


while True:
    solve()

