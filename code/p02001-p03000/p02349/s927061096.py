# -*- coding: utf-8 -*-
"""
Range Add Query (RAQ)
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E&lang=ja

"""
import sys


def main(args):
    def add(b, k, x):
        while k <= n:
            b[k] += x
            k += k & -k

    def get(b, k):
        s = 0
        while k > 0:
            s += b[k]
            k -= k & -k
        return s

    n, queries = map(int, input().split())
    bit0 = [0] * (n + 1)
    bit1 = [0] * (n + 1)

    for _ in range(queries):
        q, *args = input().split()
        args = [int(a) for a in args]
        if q == '1':
            res = get(bit0, args[0]) + get(bit1, args[0]) * args[0]
            res -= get(bit0, args[0] - 1) + get(bit1, args[0] - 1) * (args[0] - 1)
            print(res)
        else:
            add(bit0, args[0], -args[2] * (args[0] - 1))
            add(bit1, args[0], args[2])
            add(bit0, args[1] + 1, args[2]* args[1])
            add(bit1, args[1] + 1, -args[2])


if __name__ == '__main__':
    main(sys.argv[1:])

