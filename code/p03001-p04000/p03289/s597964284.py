import sys
import socket
from collections import Counter

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
    s = read_str()
    res = 'WA'
    if s[0] == 'A':
        c = 0
        for letter in s[2:-1]:
            if letter == 'C':
                c += 1
        if c == 1:
            upper = 0
            for letter in s:
                if letter.lower() != letter:
                    upper += 1
            if upper == 2:
                res = 'AC'
    print(res)


main()
