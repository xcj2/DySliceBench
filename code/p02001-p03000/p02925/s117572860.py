# -*- coding: utf-8 -*-
from collections import Counter, defaultdict


import sys
# sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 1 << 60


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        ep(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, A):
    g = defaultdict(list)
    rg = Counter()

    V = set()

    def ij2v(i, j):
        if i > j:
            i, j = j, i
        return i * 10**6 + j
    for i, a in enumerate(A, start=1):
        for j in range(len(a)-1):
            u = ij2v(i, a[j])
            v = ij2v(i, a[j+1])
            g[u].append(v)
            rg[v] += 1
            V.add(u)
            V.add(v)

    s = []
    for v in V:
        if not rg[v]:
            s.append(v)

    done = len(s)
    ans = 0
    while s:
        ans += 1
        ns = []
        for u in s:
            for v in g[u]:
                rg[v] -= 1
                if rg[v] == 0:
                    ns.append(v)
                    done += 1
        s = ns

    if done != N * (N-1) // 2:
        return -1

    return ans



def main():
    N = read_int()
    A = [read_int_n() for _ in range(N)]
    print(slv(N, A))


if __name__ == '__main__':
    main()
