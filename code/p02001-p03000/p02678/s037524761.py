# -*- coding: utf-8 -*-
from collections import Counter, defaultdict, deque



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


@mt
def slv(N, M, AB):
    g = defaultdict(list)
    for a, b in AB:
        g[a].append(b)
        g[b].append(a)

    q = deque()
    q.append(1)
    d = {}
    d[1] = 0
    prev = {}
    while q:
        u = q.popleft()
        for v in g[u]:
            if v in d:
                continue
            d[v] = d[u] + 1
            prev[v] = u
            q.append(v)
    print('Yes')
    return [prev[i] for i in range(2, N+1)]


def main():
    N, M = read_int_n()
    AB = [read_int_n() for _ in range(M)]
    print(*slv(N, M, AB), sep='\n')


if __name__ == '__main__':
    main()
