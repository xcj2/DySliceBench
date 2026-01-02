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
    s = read_str()
    n = len(s)
    res = 0
    w = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'B':
            res += w
        else:
            w += 1
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
