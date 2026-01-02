import sys
import socket

if socket.gethostname() in ['N551J', 'F551C']:
    sys.stdin = open('a1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve():
    n, x = read_int_list()
    a = read_int_list()
    a.sort()
    if sum(a) == x:
        return n
    res = 0
    for i in range(n):
        if sum(a[:i]) <= x:
            res = i
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
