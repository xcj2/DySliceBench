# -*- coding: utf-8 -*-
import bisect
import sys

sys.setrecursionlimit(10**6)
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
def slv(N, A, UV):
    A.insert(0, -1)
    g = [list() for _ in range(0, N+1)]
    for u, v in UV:
        g[u].append(v)
        g[v].append(u)

    ans = [-1] * (N+1)
    ans[1] = 1
    dp = [INF] * (N+1)
    dp[0] = A[1]

    def dfs(u, p):
        for v in g[u]:
            if v == p:
                continue

            i = bisect.bisect_left(dp, A[v])
            b = dp[i]
            dp[i] = A[v]
            ans[v] = bisect.bisect_left(dp, INF)
            dfs(v, u)
            dp[i] = b

    dfs(1, 0)

    for i in range(1, N+1):
        print(ans[i])


def main():
    N = read_int()
    A = read_int_n()
    UV = [read_int_n() for _ in range(N-1)]
    slv(N, A, UV)


if __name__ == '__main__':
    main()
