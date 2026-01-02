import sys
from collections import defaultdict
from queue import deque
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    N, M, L = geta(int)
    INF = 10**10

    d = [[INF] * (N + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        d[i][i] = 0

    for _ in range(M):
        a, b, c = geta(int)
        d[a][b] = c
        d[b][a] = c

    def warshall_froyd(_d):
        for k in range(1, N + 1):
            for i in range(1, N + 1):
                for j in range(1, N + 1):
                    l = _d[i][k] + _d[k][j]
                    if _d[i][j] > l:
                        _d[i][j] = l

    warshall_froyd(d)

    f = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        f[i][i] = 0
        for j in range(N + 1):
            if d[i][j] <= L:
                f[i][j] = 1

    warshall_froyd(f)

    for _ in range(gete(int)):
        s, t = geta(int)
        ret = f[s][t]
        print(ret - 1 if ret != INF else -1)


if __name__ == "__main__":
    main()