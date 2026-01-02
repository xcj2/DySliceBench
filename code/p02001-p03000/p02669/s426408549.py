# -*- coding: utf-8 -*-
from functools import lru_cache

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


# @mt
def slv(N, A, B, C, D):
    @lru_cache(maxsize=None)
    def f(n):
        ans = n*D
        for i in range(-min(2, n), min(3, n)):
            m = n + i
            i = abs(i)
            if m == 0:
                continue

            if m % 5 == 0:
                ans = min(ans, f(m//5) + C + D*i)
            if m % 3 == 0:
                ans = min(ans, f(m//3) + B + D*i)
            if m % 2 == 0:
                ans = min(ans, f(m//2) + A + D*i)
        return ans

    return f(N)


def main():
    T = read_int()
    for _ in range(T):
        N, A, B, C ,D = read_int_n()
        print(slv(N, A, B, C, D))


if __name__ == '__main__':
    main()
