import sys
import socket

hostnames = ['N551J', 'F551C', 'X553M']
input_file = 'c1.in'
if socket.gethostname() in hostnames:
    sys.stdin = open(input_file)


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve():
    inf = 10 ** 20
    n = read_int()
    x = read_int_list()
    res = inf
    for p in range(1, 101):
        s = 0
        for i in range(n):
            s += (p - x[i]) ** 2
        if res > s:
            res = s
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
