import sys
import socket

if socket.gethostname() == 'N551J':
    sys.stdin = open('b1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve():
    n, m, k = read_int_list()
    for i in range(n+1):
        for j in range(m+1):
            if i * j + (n - i) * (m - j) == k:
                return 'Yes'
    return 'No'


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
