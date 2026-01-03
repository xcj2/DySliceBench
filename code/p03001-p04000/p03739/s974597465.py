import sys

# sys.stdin = open('c1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


n = read_int()
a0 = read_int_list()
res = 10 ** 20
for first in [-1, 1]:
    a = list(a0)
    sign = first
    r = 0
    s = 0
    for i in range(n):
        if (s + a[i]) * sign <= 0:
            if sign < 0:
                dif = s + a[i] + 1
                a[i] -= dif
                r += dif
            if sign > 0:
                dif = -(s + a[i]) + 1
                a[i] += dif
                r += dif
        sign *= -1
        s += a[i]
    if res > r:
        res = r
print(res)
