import sys
from collections import Counter


# sys.stdin = open('c1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def solve():
    n, m = read_int_list()
    c = Counter()
    for i in range(m):
        a, b = read_int_list()
        if a == 1:
            c[b] += 1
        if b == n:
            c[a] += 1

    if 2 in c.values():
        return 'POSSIBLE'
    return 'IMPOSSIBLE'


res = solve()
print(res)
