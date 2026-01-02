import socket
import sys

hostnames = ['N551J', 'F551C', 'X553M']
input_file = 'b1.in'
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
    n, k = read_int_list()
    res = 0
    while n > 0:
        n //= k
        res += 1
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
