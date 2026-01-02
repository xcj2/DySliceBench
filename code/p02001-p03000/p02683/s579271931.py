import collections
import functools

import sys

input = lambda: sys.stdin.readline()


def cin_int_list():
    return [int(x) for x in input().split()]


def cin_int_iter():
    return (int(x) for x in input().split())


def cin_int():
    return int(input())


def cout_int_iter(a):
    print(' '.join(map(str, a)))


def iota(n, start=0):
    return list(range(start, n))


def cin_digits_list():
    return [ord(x) - ord('0') for x in input()]


def main():
    n, m, x = cin_int_iter()

    c = [0] * n
    a = [[0] * m for _ in range(n)]

    cnt = collections.Counter()

    for i in range(n):
        tmp = list(map(int, input().split()))

        c[i] = tmp[0]

        for alg, level in enumerate(tmp[1:]):
            a[i][alg] = level

            cnt[alg] += level

    for alg in range(m):
        if cnt[alg] < x:
            print('-1')
            return

    mem = {}

    def search(i, read, levels, cost):
        if all(level >= x for level in levels):
            return cost

        if i == n:
            return float('inf')

        key = (i, read)
        if key in mem:
            return mem[key]

        ret = min(
            search(i + 1, read | 1 << i, [levels[j] + a[i][j] for j in range(m)], cost + c[i]),
            search(i + 1, read, levels, cost)
        )

        mem[key] = ret

        return ret

    print(search(0, 0, [0 for i in range(m)], 0))


main()
