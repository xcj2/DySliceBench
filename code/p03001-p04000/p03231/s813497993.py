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


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve():
    n, m = read_int_list()
    a = read_str()
    b = read_str()
    d = gcd(n, m)
    if a[::n // d] == b[::m // d]:
        lcm = n * m // d
        return lcm
    return -1


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
