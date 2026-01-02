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
def slv(S, T):
    if len(set(c for c in T) - set(c for c in S)) > 0:
        return -1

    from collections import defaultdict
    si = defaultdict(list)
    for i, c in enumerate(S):
        si[c].append(i)

    ans = 0
    ci = 0
    from bisect import bisect_left
    for i, c in enumerate(T):
        j = bisect_left(si[c], ci)
        if j == len(si[c]):
            j = 0
            ans += 1
        ci = si[c][j] + 1
    return (ans)*len(S) + ci





def main():
    S = read_str()
    T = read_str()
    print(slv(S, T))


if __name__ == '__main__':
    main()
