# -*- coding: utf-8 -*-
import sys
from collections import Counter
# sys.setrecursionlimit(100000)
# input = sys.stdin.buffer.readline
INF = 2**62-1

def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


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
def slv(S):
    # 2019 = 3 * 673
    L = 2019
    rl = [0] * L
    rl[0] = 1
    ans = 0
    for c in S:
        n = int(c)
        nrl = [0] * L
        nrl[0] = 1
        for r in range(L):
            m = rl[r]
            r = (r * 10 + n) % 2019
            if r == 0:
                ans += m
            nrl[r] += m
        rl = nrl
        # print(rl)

    return ans


def main():
    S = read_str()
    print(slv(S))

    # import random
    # S = ''.join(map(str, random.choices(range(1, 10), k=2*10**5)))
    # print(slv(S))


if __name__ == '__main__':
    main()
