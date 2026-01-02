import sys
import socket

if socket.gethostname() in ['N551J', 'F551C']:
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
    n = read_int()
    a = read_int_list()
    M = 10 ** 9 + 7

    # Compute all inverse modulo M
    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (-(M // i) * inv[M % i]) % M

    c = [0] * (n + 1)
    for i in range(n):
        c[i + 1] = (c[i] + inv[i + 1]) % M

    # The same as B in the editorial
    b = [0] * n
    for i in range(n):
        b[i] = (c[i + 1] + c[n - i] - 1) % M

    f = 1
    for i in range(1, n + 1):
        f = (f * i) % M

    res = 0
    for i in range(n):
        res = (res + f * b[i] * a[i]) % M
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
