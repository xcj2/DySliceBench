import sys
from collections import Counter

from functools import reduce

# sys.stdin = open('a1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int_list():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


s = read_str()
n = len(s)
c = [set() for l in s]
for i in range(n, 0, -1):
    d = n - i
    for j in range(i):
        c[j].add(s[j + d])
    intersection = reduce(lambda x, y: x & y, c[:i])
    if intersection:
        print(d)
        break
