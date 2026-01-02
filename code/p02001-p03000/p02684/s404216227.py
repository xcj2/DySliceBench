#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
ACMOD = 1000000007
INF = 1 << 62


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


def main():
    N, K = lmi()
    A = lmi()
    c = [-1] * N
    current = 0
    d = dict()
    d[0] = 0
    c[0] = 0
    count = 0
    loop_start = -1
    for count in range(1,2 * N+2):
        _next = A[current] - 1
        c[_next] = count
        d[count] = _next
        current = _next
    for i in reversed(range(N)):
        if d[i] == d[N]:
            loop_size = N- i
            break
    if K <= 2*N:
        print(d[K] + 1)
    else:
        print(d[(K - N) % loop_size + N] + 1)
    # print(loop_size,loop_start)
    # print(c, d, loop_size, loop_start, loop_size)
    # print(d[K % loop_size] + 1)


if __name__ == '__main__':
    main()
