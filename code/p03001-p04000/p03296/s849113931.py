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
    n = read_int()
    a = read_int_list()
    res = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and a[j - 1] == a[j]:
            j += 1
        l = j - i
        res += l // 2
        i = j
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
