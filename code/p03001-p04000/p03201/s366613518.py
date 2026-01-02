import sys
import socket
from collections import Counter

if socket.gethostname() in ['N551J', 'F551C']:
    sys.stdin = open('b1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve():
    res = 0
    n = read_int()
    a = read_int_list()
    a.sort()
    c = Counter(a)
    for i in range(n - 1, -1, -1):
        if c[a[i]] <= 0:
            continue
        c[a[i]] -= 1
        p = 1
        while not p <= a[i] < 2 * p:
            p *= 2
        comp = 2 * p - a[i]
        if c[comp] > 0:
            c[comp] -= 1
            res += 1
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
