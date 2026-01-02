import sys
sys.setrecursionlimit(1000000)

n = int(input())
e = [[] for _ in range(n)]
weights = {}
for i in range(n-1):
    s, t, w = map(int, input().split())
    e[s].append(t)
    e[t].append(s)
    weights[(s, t)] = w
    weights[(t, s)] = w


def dfs(v, d, visited):
    r = [d, v]
    visited[v] = True
    for tv in e[v]:
        if not visited[tv]:
            r = max([dfs(tv, d+weights[(v, tv)], visited), r])
    return r


def fartheast(v):
    visited = [False]*n
    return dfs(v, 0, visited)


def diameter(a, b, d, visited):
    visited[a] = True
    for tv in e[a]:
        if not visited[tv]:
            td = diameter(tv, b, d+weights[(a, tv)], visited)
            if td > 0:
                return td
    return d if a == b else 0


xd, x = fartheast(0)
yd, y = fartheast(x)
print(yd)

