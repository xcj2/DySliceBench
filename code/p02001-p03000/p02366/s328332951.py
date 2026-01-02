import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30


def make_adj_list():
    n, E = map(int, input().strip().split()) # 頂点の数
    l = [[] for _ in range(n)] # 隣接リスト. 各要素は(コスト、to_node)
    for i in range(E):
        s, t = map(int, input().strip().split())
        l[s].append(t)
        l[t].append(s)

    return l, n, E

G = []
prenum = []
parent = []
lowest = []
order = 1
visited = []

def dfs(v, fr):
    global G, prenum, parent, lowest, order, visited
    visited[v] = True
    prenum[v] = lowest[v] = order
    order += 1
    
    for node in G[v]:
        if not visited[node]:
            parent[node] = v
            dfs(node, v)
            lowest[v] = min(lowest[v], lowest[node]) # DFS Treeの子
        elif node != fr:
            lowest[v] = min(lowest[v], prenum[node]) # back edge


def main():
    global G, prenum, parent, lowest, visited
    ans = set()
    G, n, e = make_adj_list()
    prenum = [INF] * n
    parent = [INF] * n
    lowest = [INF] * n
    visited = [False] * n
    dfs(0, -1)

    c = 0
    for i in range(1, n):
        p = parent[i]
        if p == 0:
            c += 1
        elif prenum[p] <= lowest[i]:
            ans.add(p)
    if c >= 2:
        ans.add(0)
    ans = sorted(list(ans))
    for i in ans:
        print(i)


if __name__ == '__main__':
    main()

