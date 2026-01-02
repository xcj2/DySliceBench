import sys
from itertools import combinations
from collections import defaultdict

sys.setrecursionlimit(100000000)

class UnionFind(object):
    def __init__(self, N):
        self._parent = list(range(N))
        self.__num_components = [1] * N

    def root(self, x):
        if self._parent[x] == x:
            return x
        else:
            # root abbreviation
            self._parent[x] = self.root(self._parent[x])
            return self._parent[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def num_connected(self, x):
        return self.__num_components[self.root(x)]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if (x == y):
            return
        rank_x = self.__num_components[x]
        rank_y = self.__num_components[y]
        if rank_x < rank_y:
            self._parent[x] = y
            self.__num_components[y] += rank_x
        else:
            self._parent[y] = x
            self.__num_components[x] += rank_y
        return


fin = sys.stdin.readline

N = int(fin())
coordinates = [[int(elem) for elem in fin().split()] + [i] for i in range(N)]

# p, qのペアを計算
all_dists = defaultdict(list)
for each_pair in combinations(coordinates, 2):
    each_p = each_pair[0][0]-each_pair[1][0]
    each_q = each_pair[0][1] - each_pair[1][1]
    if each_p < 0:
        each_p = -each_p
        each_q = -each_q
    if each_p * each_q == 0:
        each_p = abs(each_p)
        each_q = abs(each_q)
    each_pq = (each_p, each_q)
    all_dists[each_pq].append([each_pair[0][2], each_pair[1][2]])

# 適当にスタート，探索を行う
count_list = []
for each_pq in all_dists:
    uf = UnionFind(N)
    for x, y in all_dists[each_pq]:
        uf.unite(x, y)
    num_distinct_components = 0
    for i in range(N):
        if uf.root(i) == i:
            num_distinct_components += 1
    count_list.append(num_distinct_components)

if len(count_list) == 0:
    print(1)
else:
    print(max(min(count_list), 1))
