# -*- coding: utf-8 -*-
import queue
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
def slv(N, C):
    mod = 10**9 + 7
    if N == 1:
        return (C[0] * 2) % mod

    C.sort()
    ans = 0
    a = pow(2, N, mod)
    b = pow(2, N-1, mod)
    c = pow(2, N-2, mod)
    for i in range(N):
        d = (N-i-1) * c
        d %= mod
        n = a * (b + d)
        n %= mod
        ans += n * C[i]
        ans %= mod

    return ans % mod




def main():
    N = read_int()
    C = read_int_n()
    print(slv(N, C))


if __name__ == '__main__':
    main()
