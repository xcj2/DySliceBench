import sys
# import math, string, itertools, fractions, heapq, collections, re, array, bisect, copy, functools, random
from collections import deque, defaultdict, Counter; from heapq import heappush, heappop
# from itertools import permutations, combinations, product, accumulate, groupby
# from bisect import bisect_left, bisect_right, insort_left, insort_right
from operator import itemgetter as ig
sys.setrecursionlimit(10 ** 7)
# inf = 10 ** 20; INF = float("INF"); ans = 0; tmp = 0; ansli = []; tmpli = []; candili = []; mod = 10 ** 9 + 7
# dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]; ddn = dd + [(-1, 1), (1, 1), (1, -1), (-1, -1)]; ddn9 = ddn + [(0, 0)]
"""for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""
def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]#WideIntPoint
def ws(): return sys.stdin.readline().split()
def i(): return int(sys.stdin.readline())
def s(): return input()
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]

n, m, s, t = wi()
uvab = mi(m)

dists = []
distt = []
for i in range(m):
    dists.append([uvab[i][0], uvab[i][1], uvab[i][2]])
    distt.append([uvab[i][0], uvab[i][1], uvab[i][3]])

class Graph(object):
    """
    隣接リストによる有向グラフ
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def __len__(self):
        return len(self.graph)

    def add_edge(self, src, dst, weight=1):
        self.graph[src].append((dst, weight))

    def get_nodes(self):
        return self.graph.keys()


class Dijkstra(object):
    """
    ダイクストラ法（二分ヒープ）による最短経路探索
    計算量: O((E+V)logV)
    """

    def __init__(self, graph, start):
        self.g = graph.graph

        # startノードからの最短距離
        # startノードは0, それ以外は無限大で初期化
        self.dist = defaultdict(lambda: float('inf'))
        self.dist[start] = 0

        # 最短経路での1つ前のノード
        self.prev = defaultdict(lambda: None)

        # startノードをキューに入れる
        self.Q = []
        heappush(self.Q, (self.dist[start], start))

        while self.Q:
            # 優先度（距離）が最小であるキューを取り出す
            dist_u, u = heappop(self.Q)
            if self.dist[u] < dist_u:
                continue
            for v, weight in self.g[u]:
                alt = dist_u + weight
                if self.dist[v] > alt:
                    self.dist[v] = alt
                    self.prev[v] = u
                    heappush(self.Q, (alt, v))

    def shortest_distance(self, goal):
        """
        startノードからgoalノードまでの最短距離
        """
        return self.dist[goal]

    def shortest_path(self, goal):
        """
        startノードからgoalノードまでの最短経路
        """
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = self.prev[node]
        return path[::-1]
# (src, dst, weight)
inputs = dists
inputt = distt

gs = Graph()
gt = Graph()
for src, dst, weight in inputs:
    gs.add_edge(src, dst, weight)
    gs.add_edge(dst, src, weight)
for src, dst, weight in inputt:
    gt.add_edge(src, dst, weight)
    gt.add_edge(dst, src, weight)

spdi = {}
tpdi = {}
ds = Dijkstra(gs, s)
dt = Dijkstra(gt, t)
for i in range(1, n + 1):
    sp = format(ds.shortest_distance(i))
    spdi[i] = int(sp)
    tp = format(dt.shortest_distance(i))
    tpdi[i] = int(tp)
#print('最短経路: {}'.format(d.shortest_path(1)))
#print('最短距離: {}'.format(d.shortest_distance(1)))
route = []
for i in range(1, n + 1):
    route.append([10 ** 15 - (spdi[i] + tpdi[i]), i])
route.sort(key=ig(0), reverse=True)
j = 0
for i in range(n):
    while j < n:
        if i < route[j][1]:
            print(route[j][0])
            break
        else:
            j += 1
    if j == n:
        print(route[j][0])