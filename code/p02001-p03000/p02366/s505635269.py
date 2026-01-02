from sys import setrecursionlimit

setrecursionlimit(1000000)


def art_points(n, m, G):
    def dfs(cur, prev):
        nonlocal t
        prenum[cur] = lowest[cur] = t
        t += 1
        visited[cur] = True

        for ne in G[cur]:
            if not visited[ne]:
                parent[ne] = cur
                dfs(ne, cur)
                lowest[cur] = min(lowest[cur], lowest[ne])
            elif ne != prev:
                lowest[cur] = min(lowest[cur], prenum[ne])

    t = 1
    prenum = [0] * n
    parent = [0] * n
    lowest = [0] * n
    visited = [False] * n
    dfs(0, -1)

    ap = set()
    np = 0
    for i, p in zip(range(1, n), parent[1:]):
        if p == 0:
            np += 1
        elif prenum[p] <= lowest[i]:
            ap.add(p)
    if np > 1:
        ap.add(0)
    return ap


def main():
    n, m = [int(x) for x in input().split()]
    G = [[] for _ in range(n)]
    for _ in range(m):
        s, t = [int(x) for x in input().split()]
        G[s].append(t)
        G[t].append(s)
    for p in sorted(art_points(n, m, G)):
        print(p)


main()

