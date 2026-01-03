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


def main():
    n = read_int()
    a = read_int_list()
    a.sort()
    c = Counter(a)
    l = set()
    for i in a:
        if c[i] >= 2:
            l.add(i)
    l = list(l)
    l.sort()

    res = 0
    if len(l) >= 1:
        m = l[-1]
        if c[m] >= 4:
            res = m * m
        else:
            if len(l) >= 2:
                p = l[-2]
                res = m * p
    print(res)


main()
