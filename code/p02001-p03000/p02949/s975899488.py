# -*- coding: utf-8 -*-
import sys
# sys.setrecursionlimit(10**6)
# buff_readline = sys.stdin.buffer.readline
buff_readline = sys.stdin.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def read_float():
    return float(buff_readline())


def read_float_n():
    return list(map(float, buff_readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


from collections import defaultdict

def BellmanFord(g, s, N):
    dist = [INF] * (N+1)
    dist[s] = 0
    for i in range(N):
        for u in range(1, N+1):
            if dist[u] == INF:
                continue
            for v in g[u]:
                if dist[v] > dist[u] + g[u][v]:
                    dist[v] = dist[u] + g[u][v]
    for i in range(N//2):
        for u in range(1, N+1):
            if dist[u] == INF:
                continue
            for v in g[u]:
                if dist[v] > dist[u] + g[u][v]:
                    if dist[v] != INF:
                        dist[v] = -INF
    return dist


@mt
def slv(N, M, P, ABC):
    g = defaultdict(dict)
    for a, b, c in ABC:
        if a in g and b in g[a]:
            g[a][b] = min(g[a][b], -(c - P))
        else:
            g[a][b] = -(c - P)

    d = BellmanFord(g, 1, N)
    if -d[N] >= INF:
        return -1
    return max(0, -d[N])





def main():
    N, M, P = read_int_n()
    ABC = [read_int_n() for _ in range(M)]
    print(slv(N, M, P, ABC))


if __name__ == '__main__':
    main()
