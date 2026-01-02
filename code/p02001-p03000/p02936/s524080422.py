import sys


sys.setrecursionlimit(10 ** 6)


def solve():
    def dfs(v):
        print(counter)
        for nv in g[v]:
            if nv in visited:
                continue
            visited.add(nv)
            counter[nv] += counter[v]
            dfs(nv)

    def input():
        return sys.stdin.readline().strip()

    N, Q = map(int, input().split())
    g = [set() for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].add(b)
        g[b].add(a)
    counter = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        counter[p] += x

    stack = [0]
    visited = {0}
    while stack:
        v = stack.pop()
        for nv in g[v]:
            if nv in visited:
                continue
            stack.append(nv)
            visited.add(nv)
            counter[nv] += counter[v]
    return counter


print(" ".join(map(str, solve())))
