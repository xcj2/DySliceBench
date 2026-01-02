# -*- coding: utf-8 -*-
from functools import lru_cache

import sys
sys.setrecursionlimit(10**6)
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
def slv(N, X):
    @lru_cache(maxsize=None)
    def f(y):
        c = bin(y).count('1')
        if c == 0:
            return 0
        r = y % c

        return 1 + f(r)

    C = X.count('1')
    cmr = 0
    cpr = 0
    for b in X:
        cmr *= 2
        cmr += int(b)
        if C-1 == 0:
            cmr = 0
        else:
            cmr %= C - 1
        cpr *= 2
        cpr += int(b)
        cpr %= C + 1

    bp = 1
    bm = 1

    ans = []
    for i in range(N-1, -1, -1):
        t = 1
        if X[i] == '0':
            x = (cpr + bp) % (C+1)
        else:
            if C-1 == 0:
                x = 0
                t = 0
            else:
                x = (cmr - bm) % (C-1)
        while True:
            c = bin(x).count('1')
            # print(x, c)
            if c == 0:
                break
            x = x % c
            t += 1
        ans.append(t)

        bp *= 2
        bp %= (C+1)
        if C - 1 != 0:
            bm *= 2
            bm %= (C-1)

    for a in reversed(ans):
        print(a)


def main():
    N = read_int()
    X = read_str()
    slv(N, X)

    # import random
    # N = 10**5
    # N *= 2
    # X = ''.join(random.choices('01', k=N))
    # print(slv(N, X))




if __name__ == '__main__':
    main()
