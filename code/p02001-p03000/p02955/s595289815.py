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


def divisor(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i


@mt
def slv(N, K, A):
    S = sum(A)
    ans = 0
    for d in divisor(S):
        r = [a%d for a in A]
        r.sort()
        lr = [0]
        rr = [0]
        for v in r:
            lr.append(lr[-1] + v)
            rr.append(rr[-1] + (d-v))
        for i in range(N):
            l = lr[i+1] - lr[0]
            r = rr[-1] - rr[i+1]
            if l == r and l <= K:
                ans = max(ans, d)
    return ans






def main():
    N, K = read_int_n()
    A = read_int_n()
    print(slv(N, K, A))


if __name__ == '__main__':
    main()
