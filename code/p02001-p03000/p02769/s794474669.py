import socket
import sys

hostnames = ['N551J', 'F551C', 'X553M']
input_file = 'e1.in'
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


mod = 10 ** 9 + 7

N = 4 * 10 ** 5
f = [1] * (N + 1)
for i in range(N):
    f[i + 1] = ((i + 1) * f[i]) % mod

MAX = N + 2
inv = [0] * MAX
inv[1] = 1
for i in range(2, MAX):
    inv[i] = - inv[mod % i] * (mod // i)
    inv[i] %= mod


def solve():
    n, K = read_int_list()
    if K >= n:
        K = n - 1
    r = 0
    c = 1
    d = 1
    for k in range(K + 1):
        r += c * d
        r %= mod
        c = (c * (n - 1 - k) * inv[k + 1]) % mod
        d = (d * (n - k) * inv[k + 1]) % mod

    return r


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
