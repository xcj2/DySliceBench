# -*- coding: utf-8 -*-
import sys
buff_readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 2**62-1


def read_int():
    return int(buff_readline())


def read_int_n():
    return list(map(int, buff_readline().split()))


def slv(N, M, H, AB):
    g = [list() for _ in range(N+1)]
    for a, b in AB:
        g[a].append(b)
        g[b].append(a)

    ans = 0
    for u in range(1, N+1):
        h = H[u-1]
        for v in g[u]:
            if H[v-1] >= h:
                break
        else:
            ans += 1

    return ans


def main():
    N, M = read_int_n()
    H = read_int_n()
    AB = [read_int_n() for _ in range(M)]
    print(slv(N, M, H, AB))


if __name__ == '__main__':
    main()
