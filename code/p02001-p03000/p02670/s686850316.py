# -*- coding: utf-8 -*-
import sys
buff_readline = sys.stdin.buffer.readline


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def slv(N, P):
    M = N+2
    cost = [0] * M**2
    occupy = [1] * M**2
    for i in range(N):
        im = i*M + M + 1
        for j in range(N):
            cost[im+j] = min(i, j, N-i-1, N-j-1)

    ds = [-1, 1, -M, M]
    ans = 0
    for p in P:
        p -= 1
        x = p // N
        y = p % N
        p = x * M + y + M + 1
        ans += cost[p]
        occupy[p] = 0
        s = []
        s.append(p)
        while s:
            pi = s.pop()
            for d in ds:
                ni = pi + d
                nc = cost[pi] + occupy[pi]
                if nc < cost[ni]:
                    cost[ni] = nc
                    s.append(ni)
    return ans


def main():
    N = read_int()
    P = read_int_n()
    print(slv(N, P))


if __name__ == '__main__':
    main()
