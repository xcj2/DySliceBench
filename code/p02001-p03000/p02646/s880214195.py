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


@mt
def slv(A, V, B, W, T):
    d = abs(A-B)
    vd = V-W
    if vd <= 0:
        return 'NO'

    from fractions import Fraction
    if Fraction(d, vd) <= T:
        return 'YES'

    return 'NO'



def main():
    A, V = read_int_n()
    B, W = read_int_n()
    T = read_int()
    print(slv(A, V, B, W, T))


if __name__ == '__main__':
    main()
