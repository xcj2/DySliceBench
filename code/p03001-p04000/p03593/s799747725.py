import sys
import socket
from collections import Counter

hostname = socket.gethostname()

if hostname == 'F451C':
    sys.stdin = open('c1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def main():
    h, w = read_int_list()
    c = Counter()
    for i in range(h):
        a = read_str()
        c += Counter(a)

    n4 = (h - h % 2) * (w - w % 2) // 4
    n2 = 0
    if h % 2 == 1:
        n2 += w // 2
    if w % 2 == 1:
        n2 += h // 2
    n1 = 0
    if h % 2 == 1 and w % 2 == 1:
        n1 = 1

    v = [4] * n4 + [2] * n2 + [1] * n1
    l = list(c.values())
    for x in v:
        l.sort(reverse=True)
        if l[0] < x:
            print('No')
            return
        else:
            l[0] -= x
    print('Yes')


main()
