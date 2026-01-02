import bisect
import collections
import heapq
import itertools
import operator
import sys


def main():
    int_max = 2 ** 31 - 1
    n, q = map(int, sys.stdin.readline().split())
    n = 1 << (n - 1).bit_length()
    dat = [int_max] * 131072 * 2

    def update(i, x):
        i += n - 1
        dat[i] = x
        while i > 0:
            i = (i - 1) // 2
            dat[i] = min(dat[i * 2 + 1], dat[i * 2 + 2])

    def query(a, b, k, l, r):
        if r <= a or b <= l:
            return int_max
        if a <= l and r <= b:
            return dat[k]
        else:
            vl = query(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = query(a, b, k * 2 + 2, (l + r) // 2, r)
            return min(vl, vr)

    for _ in range(q):
        com, x, y = map(int, sys.stdin.readline().split())
        if com == 0:
            update(x, y)
        elif com == 1:
            print(query(x, y + 1, 0, 0, n))


if __name__ == "__main__":
    main()

