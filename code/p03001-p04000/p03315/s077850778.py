import sys
import socket

hostname = socket.gethostname()

if hostname == 'F451C':
    sys.stdin = open('a1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def main():
    res = 0
    s = read_str()
    if s[0] == '+':
        res += 1
    else:
        res -= 1
    if s[1] == '+':
        res += 1
    else:
        res -= 1
    if s[2] == '+':
        res += 1
    else:
        res -= 1
    if s[3] == '+':
        res += 1
    else:
        res -= 1
    print(res)


main()
