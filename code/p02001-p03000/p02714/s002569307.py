# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
from itertools import permutations
import bisect
input = sys.stdin.readline
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
def slv(N, S):
    ci = defaultdict(list)
    for i, c in enumerate(S):
        ci[c].append(i)

    ans = 0
    for c1, c2 , c3 in permutations('RGB', r=3):
        for i in ci[c1]:
            for j in range(bisect.bisect_left(ci[c2], i), len(ci[c2])):
                j = ci[c2][j]
                ans += len(ci[c3]) - bisect.bisect_left(ci[c3], j)
                d = (j-i)+j
                k = bisect.bisect_left(ci[c3], d)
                if k < len(ci[c3]) and ci[c3][k] == d:
                    ans -= 1
    return ans


def main():
    N = read_int()
    S = read_str()
    print(slv(N, S))


if __name__ == '__main__':
    main()
