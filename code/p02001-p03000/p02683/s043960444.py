# -*- coding: utf-8 -*-
from itertools import combinations, combinations_with_replacement, product, permutations


import sys
# sys.setrecursionlimit(10**6)
buff_readline = sys.stdin.buffer.readline
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
def slv(N, M, X, CA):
    A = [ca[1:] for ca in CA]
    C = [ca[0] for ca in CA]
    ans = INF
    for k in range(1, N+1):
        for i in combinations(range(N), r=k):
            m = [0] * M
            t = 0
            for j in i:
                for k, a in enumerate(A[j]):
                    m[k] += a
                t += C[j]
            if min(m) >= X:
                ans = min(ans, t)
    if ans == INF:
        ans = -1
    return ans


def main():
    N, M, X = read_int_n()
    CA = [read_int_n() for _ in range(N)]
    print(slv(N, M, X, CA))


if __name__ == '__main__':
    main()
