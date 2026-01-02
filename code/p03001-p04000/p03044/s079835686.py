import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N = gete(int)
    g = [set() for _ in range(N+1)]
    for _ in range(N-1):
        u, v, w = geta(int)
        g[u].add((v, w))
        g[v].add((u, w))

    dist = [-1] * (N+1)
    color = [-1]*(N+1)

    dist[1] = 0
    color[1] = 0

    def dfs(i, d):

        dist[i] = d
        color[i] = 0 if d & 1 == 0 else 1

        for j, wj in g[i]:
            if dist[j] < 0:
                dfs(j, d + wj)

    dfs(1, 0)

    print(*color[1:], sep="\n")


if __name__ == "__main__":
    main()
