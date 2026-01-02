# -*- coding: utf-8 -*-
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
def slv(N, S):
    b = []
    for s in S:
        bottom = 0
        cur = 0
        for c in s:
            if c == '(':
                cur += 1
            else:
                cur -= 1
            bottom = min(bottom, cur)
        b.append((bottom, cur))

    bp = [_ for _ in b if _[1] > 0]
    bn = [_ for _ in b if _[1] <= 0]
    bp.sort(key=lambda x: x[0], reverse=True)
    bn.sort(key=lambda x: x[1]-x[0], reverse=True)

    cur = 0
    for bt, ct in bp:
        if cur + bt < 0:
            return 'No'
        cur += ct

    for bt, ct in bn:
        if cur + bt < 0:
            return 'No'
        cur += ct

    if cur != 0:
        return 'No'
    return 'Yes'



def main():
    N = read_int()
    S = [read_str() for _ in range(N)]
    print(slv(N, S))


if __name__ == '__main__':
    main()
