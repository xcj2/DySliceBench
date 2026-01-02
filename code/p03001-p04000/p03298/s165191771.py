import sys
import socket

if socket.gethostname() in ['N551J', 'F551C']:
    sys.stdin = open('c1.in')


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
    s = read_str()

    cache = {}

    def rec(red, blue):
        if (red, blue) in cache:
            return cache[(red, blue)]
        nr = len(red)
        nb = len(blue)
        if nr > n or nb > n:
            res = 0
            cache[(red, blue)] = res
            return res
        if nr + nb == 2 * n:
            res = 1
            cache[(red, blue)] = res
            return res
        c = s[nr + nb]
        res = 0
        if nr + nb < n or (nr < n and c == blue[nr - n]):
            res += rec(red + c, blue)
        if nr + nb < n or (nb < n and c == red[n - 1 - nb]):
            res += rec(red, c + blue)
        cache[(red, blue)] = res
        return res

    res2 = rec('', '')
    return res2


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
