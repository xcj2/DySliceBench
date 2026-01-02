# -*- coding: utf-8 -*-
from collections import Counter, defaultdict


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
def slv(H, W, M, HW):
    g = defaultdict(dict)
    for h, w in HW:
        g[h][w] = 1
    h = Counter(h for h, w in HW)
    w = Counter(w for h, w in HW)
    h = list(h.items())
    h.sort(reverse=True, key=lambda x: x[1])
    w = list(w.items())
    w.sort(reverse=True, key=lambda x: x[1])

    ans = 0
    mh = h[0][1]
    mw = w[0][1]
    for k, v in h:
        if v != mh:
            break
        for kk, vv in w:
            if vv != mw:
                break
            if k in g and kk in g[k]:
                ans = max(ans, v + vv - 1)
            else:
                return v + vv

    return ans


def main():
    H, W, M = read_int_n()
    HW = [read_int_n() for _ in range(M)]
    print(slv(H, W, M, HW))


if __name__ == '__main__':
    main()
