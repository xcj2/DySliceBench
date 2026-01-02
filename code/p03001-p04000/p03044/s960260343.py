"""Even Relation
https://atcoder.jp/contests/abc126/tasks/abc126_d
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5 + 1)


class Node:
    def __init__(self, node_id, color):
        self.node_id = node_id
        self.color = color
        self.edges = []

class Edge:
    def __init__(self, to, length):
        self.to = to
        self.length = length


def dfs(node, p):
    for edge in node.edges:
        # 親への枝は何もしない
        if edge.to == p:
            continue
        # 枝が偶数なら子を同じ色で塗る
        if edge.length % 2 == 0:
            graph[edge.to].color = node.color
        else:
            if node.color == 1:
                graph[edge.to].color = 0
            else:
                graph[edge.to].color = 1

        dfs(graph[edge.to], node.node_id)


N = int(input())

# グラフ初期化
graph = [Node(node_id=i, color=-1) for i in range(N + 1)]
for i in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].edges.append(Edge(v, w))
    graph[v].edges.append(Edge(u, w))

# 最初は0始まり
graph[1].color = 0

dfs(graph[1], -1)


for i in range(1, N + 1):
    print(graph[i].color)
