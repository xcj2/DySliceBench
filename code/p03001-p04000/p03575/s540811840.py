def dfs(u, g, visited):
    visited[u] = True

    for v in range(len(g)):
        if visited[v]:
            continue
        if g[u][v]:
            dfs(v, g, visited)


def solve():
    [N, M] = [int(x) for x in input().split()]

    import collections

    edges = []
    g = [[False] * N for _ in range(N)]
    for i in range(M):
        a, b = [int(x) for x in input().split()]
        edges.append((a-1, b-1))
        g[a-1][b-1] = g[b-1][a-1] = True

    ans = 0
    for e in edges:
        g[e[0]][e[1]] = g[e[1]][e[0]] = False

        # print(g)
        visited = [False] * N

        dfs(0, g, visited)
        # print(visited)
        ans += not all(visited)

        g[e[0]][e[1]] = g[e[1]][e[0]] = True
    return ans


def main():
    print(solve())


if __name__ == '__main__':
    main()
