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


n, m = read_int_list()

a = [0] * m
b = [0] * m

for i in range(m):
    a[i], b[i] = read_int_list()

c = Counter()
for i in range(m):
    if a[i] == 1:
        c[b[i]] += 1
    if b[i] == n:
        c[a[i]] += 1

res = 'IMPOSSIBLE'
for i, v in c.items():
    if v == 2:
        res = 'POSSIBLE'
print(res)
