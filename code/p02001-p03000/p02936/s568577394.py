from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(1000000)


def input():
    return stdin.readline().strip()


def main():
    N, Q = map(int, input().split())
    g = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    points = [0] * N
    for _ in range(Q):
        p, x = map(int, input().split())
        p -= 1
        points[p] += x

    scores = [0] * N

    def dfs(g, v, v_prev):
        scores[v] = points[v]
        if v_prev >= 0:
            scores[v] += scores[v_prev]

        for w in g[v]:
            if w == v_prev:
                continue
            dfs(g, w, v)

    dfs(g, 0, -1)

    print(*scores)

    return


if __name__ == "__main__":
    main()
