import sys
from collections import defaultdict
from queue import deque
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N, Q = geta(int)
    g = [set() for _ in range(N + 1)]
    v = [-1 for _ in range(N + 1)]

    for _ in range(N - 1):
        a, b = geta(int)
        g[a].add(b)
        g[b].add(a)

    d = [0] * (N + 1)
    for _ in range(Q):
        p, x = geta(int)
        d[p] += x

    def dfs(i, c):
        c2 = c + d[i]
        v[i] = c2
        for j in g[i]:
            if v[j] < 0:
                dfs(j, c2)

    dfs(1, 0)

    print(*v[1:], sep=" ")


if __name__ == "__main__":
    main()