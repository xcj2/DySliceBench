import socket
import sys

hostnames = ['N551J', 'F551C', 'X553M']
input_file = 'd1.in'
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
N = 2 * 10 ** 5
MAX = N + 2
inv = [0] * MAX
inv[1] = 1
for i in range(2, MAX):
    inv[i] = - inv[mod % i] * (mod // i)
    inv[i] %= mod


def solve():
    n, a, b = read_int_list()
    total = pow(2, n, mod)
    res = total - 1
    c = 1
    for i in range(b):
        c = (c * (n - i) * inv[i + 1]) % mod
        if i == a - 1:
            res -= c
    res -= c
    res %= mod
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
