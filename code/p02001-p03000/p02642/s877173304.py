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
def slv(N, A):
    from collections import Counter
    c = Counter()
    ma = max(A)
    for a in A:
        for i in range(ma//a + 1):
            c[a*i] += 1

    ans = 0
    for a in A:
        if c[a] == 1:
            ans += 1

    return ans


def main():
    N = read_int()
    A = read_int_n()
    print(slv(N, A))

    # from random import randint
    # N = 2* (10**5)
    # A = [randint(1, 10**6) for _ in range(N)]
    # print(slv(N, A))


if __name__ == '__main__':
    main()
