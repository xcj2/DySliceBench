"""
dfs活用問題
- 2部グラフ作成
- https://atcoder.jp/contests/abc126/tasks/abc126_d
"""
from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    (u, v, w) = map(int, input().split())
    graph[u-1].append([v-1, w])
    graph[v-1].append([u-1, w])


def dfs_recursive(n, graph):
    def dfs(graph, colors, cur, depth):
        colors[cur] = depth % 2
        for child in graph[cur]:
            child_index = child[0]
            if -1 != colors[child_index]:
                continue
            dfs(graph, colors, child_index, depth + child[1])
    colors = [-1 for _ in range(n)]
    dfs(graph, colors, 0, 0)
    for i in colors:
        print(i)


def dfs_with_queue(n, grpah):
    q = deque()
    ans = [-1 for _ in range(n)]
    q.append(0)
    ans[0] = 0
    while 0 != len(q):
        v = q.popleft()
        for neigbhor in graph[v]:
            u = neigbhor[0]
            w = neigbhor[1]
            if -1 != ans[u]:
                continue
            ans[u] = (ans[v] + w) % 2
            q.append(u)
        for i in ans:
            print(i)


dfs_recursive(n, graph)
