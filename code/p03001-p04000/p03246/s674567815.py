import sys
import socket
from collections import Counter

if socket.gethostname() in ['N551J', 'F551C']:
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
    n = read_int()
    a = read_int_list()
    c = [Counter(a[k::2]) for k in range(2)]
    a, b = [c[k].most_common(1)[0] for k in range(2)]

    if a[0] != b[0]:
        return n - a[1] - b[1]
    if a[1] == n // 2 and b[1] == n // 2:
        return n // 2

    res = n
    if a[1] < n // 2:
        p, q = c[0].most_common(2)
        res = min(res, n - q[1] - b[1])
    if b[1] < n // 2:
        p, q = c[1].most_common(2)
        res = min(res, n - a[1] - q[1])

    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
