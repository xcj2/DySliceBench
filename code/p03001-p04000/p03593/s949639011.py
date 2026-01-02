import sys
import socket
from collections import Counter

if socket.gethostname() == 'N551J':
    sys.stdin = open('c1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve():
    h, w = read_int_list()
    c = Counter()
    for i in range(h):
        c += Counter(read_str())
    values = sorted(c.values(), reverse=True)
    m = [4] * ((h // 2) * (w // 2))
    if h % 2 == 1:
        m = m + [2] * (w // 2)
    if w % 2 == 1:
        m = m + [2] * (h // 2)
    if h % 2 == 1 and w % 2 == 1:
        m = m + [1]
    for v in m:
        if values[0] < v:
            return 'No'
        else:
            values[0] -= v
            if values[0] == 0:
                values.pop(0)
            else:
                values.sort(reverse=True)
    return 'Yes'


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
