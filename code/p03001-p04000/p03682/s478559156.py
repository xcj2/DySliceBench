# https://atcoder.jp/contests/abc065/tasks/arc076_b

import itertools
from collections import Counter
from collections import defaultdict
import collections
from functools import reduce
import bisect
import math
import heapq
import copy

# Union find
class UnionFind():
    def __init__(self,size):
        self.table = [-1 for _  in range(size)]  # 負の値の場合根を表す。正の値は次の要素を返す、根まで続く
        self.size = [1 for _  in range(size)]

    #集合の代表を求める
    def find(self,x):
        while self.table[x] >= 0:
            #根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    #併合
    def union(self,x,y):
        s1 = self.find(x)#根のindex,table[s1]がグラフの高さ
        s2 = self.find(y)
        if s1 != s2:#根が異なる場合
            if self.table[s1] != self.table[s2]:#グラフの高さが異なる場合
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                    self.size[s1] += self.size[s2]
                else:
                    self.table[s1] = s2
                    self.size[s2] += self.size[s1]
            else:
                #グラフの長さが同じ場合,どちらを根にしても変わらない
                #その際,グラフが1長くなることを考慮する
                self.table[s1] += -1
                self.table[s2] = s1
                self.size[s1] += self.size[s2]
        return

    def group_size(self, x):
        return self.size[self.find(x)]

Edge = collections.namedtuple("Edge", "start end weight")


def solve_by_kraskal(n, edges):
    """
        最小全域木を計算してそのルートを返す
        Parameters
        ----------
        n : int
            頂点の数
        edges: [Edge]
            辺のリスト

        Returns
        -------
        route : [Edge]
            最小全域木を構築する辺
    """

    edges.sort(key=lambda edge: edge.weight)
    uf = UnionFind(n)
    route = []

    for edge in edges:
        if not uf.is_same(edge.start, edge.end):
            uf.union(edge.start, edge.end)
            route.append(edge)

    return route


def main():
    N = int(input())
    x_dots = []
    for i in range(N):
        x, y = map(int, input().split())
        x_dots.append((i, x, y))

    x_dots.sort(key=lambda x: x[1])
    y_dots = copy.copy(x_dots)
    y_dots.sort(key=lambda x: x[2])
    # print(x_dots)
    # print(y_dots)

    x_edges = []
    for i in range(N - 1):
        dot = x_dots[i]
        next_dot = x_dots[i + 1]
        x_edges.append(Edge(dot[0], next_dot[0], min(abs(dot[1] - next_dot[1]), abs(dot[2] - next_dot[2]))))
        x_edges.append(Edge(next_dot[0], dot[0], min(abs(dot[1] - next_dot[1]), abs(dot[2] - next_dot[2]))))

    y_edges = []
    for i in range(N - 1):
        dot = y_dots[i]
        next_dot = y_dots[i + 1]
        y_edges.append(Edge(dot[0], next_dot[0], min(abs(dot[1] - next_dot[1]), abs(dot[2] - next_dot[2]))))
        y_edges.append(Edge(next_dot[0], dot[0], min(abs(dot[1] - next_dot[1]), abs(dot[2] - next_dot[2]))))

    route = solve_by_kraskal(N, x_edges + y_edges)
    ans = 0
    for r in route:
        ans += r[2]

    print(ans)


if __name__ == '__main__':
    main()
