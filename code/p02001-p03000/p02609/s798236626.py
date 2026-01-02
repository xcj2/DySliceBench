# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**6)
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
def slv(N, X):
    C = X.count('1')
    cmr = 0
    cpr = 0
    for b in X:
        if C-1 != 0:
            cmr = ((cmr * 2) + int(b)) % (C-1)
        cpr = ((cpr * 2) + int(b)) % (C+1)

    ans = []
    for i in range(N):
        t = 1
        if X[i] == '0':
            x = (cpr + pow(2, N-i-1, C+1)) % (C+1)
        elif X[i] == '1' and C-1 != 0:
            x = (cmr - pow(2, N-i-1, C-1)) % (C-1)
        else:
            x = 0
            t = 0

        while x != 0:
            x = x % bin(x).count('1')
            t += 1

        ans.append(t)

    return ans


def main():
    N = read_int()
    X = read_str()
    print(*slv(N, X), sep='\n')


if __name__ == '__main__':
    main()
