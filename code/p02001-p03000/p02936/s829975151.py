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


class Mod:
    def __init__(self, m):
        self.m = m

    def add(self, a, b):
        return (a + b) % self.m

    def sub(self, a, b):
        return (a - b) % self.m

    def mul(self, a, b):
        return ((a % self.m) * (b % self.m)) % self.m

    def div(self, a, b):
        return self.mul(a, pow(b, self.m-2, self.m))

    def pow(self, a, b):
        return pow(a, b, self.m)


@mt
def slv(N, Q, AB, PX):
    from collections import defaultdict
    g = defaultdict(set)
    for a, b in AB:
        g[a].add(b)
        g[b].add(a)

    C = [0] * (N+1)
    for p, x in PX:
        C[p] += x

    s = [(1, -1)]
    while s:
        u, p = s.pop()
        for v in g[u]:
            if v == p:
                continue
            s.append((v, u))
            C[v] += C[u]
    return C[1:]







def main():
    N, Q = read_int_n()
    AB = [read_int_n() for _ in range(N-1)]
    PX = [read_int_n() for _ in range(Q)]
    print(*slv(N, Q, AB, PX))


if __name__ == '__main__':
    main()
