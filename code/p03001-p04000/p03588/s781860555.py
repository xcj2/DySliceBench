import sys
import socket

hostname = socket.gethostname()

if hostname == 'F451C':
    sys.stdin = open('b1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def main():
    n = read_int()
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = read_int_list()

    m = min(b)
    for i in range(n):
        if b[i] == m:
            res = a[i] + b[i]
    print(res)


main()
