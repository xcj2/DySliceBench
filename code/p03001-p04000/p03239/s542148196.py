import sys
import socket

hostname = socket.gethostname()

if hostname == 'F551C':
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
    N, T = read_int_list()
    res = 9999
    for i in range(N):
        c, t = read_int_list()
        if t <= T:
            if c < res:
                res = c
    if res == 9999:
        res = 'TLE'
    print(res)


main()
