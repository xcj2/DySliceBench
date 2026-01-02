import sys
import socket

if socket.gethostname() in ['N551J', 'F551C']:
    sys.stdin = open('d1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve0():
    h = read_int()
    m = 1
    c = 1
    while h > 1:
        h = h//2
        m *= 2
        c += m
    return c

def solve():
    h = read_int()
    m = 1
    c = 0
    while h >= 1:
        c += m
        h = h//2
        m *= 2
    return c


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
