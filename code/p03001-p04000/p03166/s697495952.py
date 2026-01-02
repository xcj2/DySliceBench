
import sys

# 再起回数上限変更
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())


class Graph(object):
    def __init__(self, n: int):
        self.adjacency_dict = {}
        self.n = n
        for i in range(n):
            self.add_vertex(i)

    def add_vertex(self, v: int):
        """ ノードを追加する """
        self.adjacency_dict[v] = []

    def add_edge(self, v1: int, v2: int, undirected=False):
        self.adjacency_dict[v1].append(v2)
        if undirected:
            self.adjacency_dict[v2].append(v1)


def find_longest(v):
    """ vからの有向最長パスをの長さをdp[v]とする """
    global dp
    if dp[v] > 0:
        return dp[v]

    res = 0
    for nv in g.adjacency_dict[v]:
        res = max(res, find_longest(nv) + 1)

    dp[v] = res
    return res


g = Graph(N)
for i in range(M):
    x, y = map(int, input().split())
    g.add_edge(x - 1, y - 1)
# print(g.adjacency_dict)

dp = [-1] * N
# gにおいて出次数が0のところのdpを0とする
for v in range(N):
    if len(g.adjacency_dict[v]) == 0:
        dp[v] = 0
# print(dp)

for v in range(N):
    find_longest(v)

print(max(dp))
