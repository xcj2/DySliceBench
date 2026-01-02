# -*- coding: utf-8 -*-
from collections import Counter, defaultdict, deque


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
def slv(H, W, K, XY1XY2, C):
    q = deque()
    s = (XY1XY2[0]-1)*W + XY1XY2[1]-1
    go = (XY1XY2[2]-1)*W + XY1XY2[3]-1
    q.append(s)
    d = {s: 0}

    while q:
        u = q.popleft()
        i = u // W
        j = u % W
        e = list()
        for k in range(1, K+1):
            if i - k >= 0 and C[i-k][j] != '@':
                n = (i-k)*W + j
                if n not in d:
                    e.append(n)
                elif d[u] +1 > d[n]:
                    break
            else:
                break
        for k in range(1, K+1):
            if i + k < H and C[i+k][j] != '@':
                n = (i+k)*W + j
                if n not in d:
                    e.append(n)
                elif d[u] + 1 > d[n]:
                    break
            else:
                break
        for k in range(1, K+1):
            if j - k >= 0 and C[i][j-k] != '@':
                n = i*W + j-k
                if n not in d:
                    e.append(n)
                elif d[u] + 1 > d[n]:
                    break
            else:
                break
        for k in range(1, K+1):
            if j + k < W and C[i][j+k] != '@':
                n = i*W + j+k
                if n not in d:
                    e.append(n)
                elif d[u] + 1 > d[n]:
                    break
            else:
                break
        for v in e:
            q.append(v)
            d[v] = d[u] + 1
            if v == go:
                return d[v]

    return -1


def main():
    H, W, K = read_int_n()
    XY1XY2 = read_int_n()

    C = [read_str() for _ in range(H)]
    print(slv(H, W, K, XY1XY2, C))

    # H = 1000
    # W = 1000
    # K = 1000
    # XY1XY2 = [1, 1, H, W]
    # C = [['.'] * W for _ in range(H)]
    # for i in range(1, H, 2):
    #     if ((i + 1) // 2) % 2 == 1:
    #         for j in range(W-1):
    #             C[i][j] = '@'
    #     else:
    #         for j in range(1, W):
    #             C[i][j] = '@'

    # # for r in C:
    # #     print(r)
    # print(slv(H, W, K, XY1XY2, C))


if __name__ == '__main__':
    main()
