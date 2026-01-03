def dfs(u, g, visited):
    # all visited
    if sum(visited) == len(visited):
        return 1

    res = 0
    for v in g[u]:
        if visited[v]:
            continue

        visited[v] = True
        # print("{} -> {}".format(u, v), visited)
        res += dfs(v, g, visited)
        visited[v] = False

    return res


def solve():
    [N, M] = [int(x) for x in input().split()]

    import collections
    g = collections.defaultdict(list)

    for i in range(M):
        a, b = [int(x) for x in input().split()]
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    visited = [False] * N
    visited[0] = True

    ans = dfs(0, g, visited)
    return ans


def main():
    print(solve())


if __name__ == '__main__':
    main()



