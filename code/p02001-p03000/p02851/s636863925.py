# -*- coding: utf-8 -*-
from collections import Counter
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


def slv(N, K, A):
    B = [0]
    for i, a in enumerate(A, start=0):
        B.append((B[-1] + a) % K)

    for i in range(len(B)):
        B[i] = (B[i] - i) % K

    ans = 0
    C = Counter()
    n = 0
    for i, b in enumerate(B):
        C[b] += 1
        n += 1
        if n > K:
            C[B[i-K]] -= 1
            n -= 1
        ans += C[b] - 1

    return ans


def main():
    N, K = read_int_n()
    A = read_int_n()
    print(slv(N, K, A))


if __name__ == '__main__':
    main()
