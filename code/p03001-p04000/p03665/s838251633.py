import sys

# sys.stdin = open('a1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve():
    n, p = read_int_list()
    a = read_int_list()
    a = map(lambda x: x % 2, a)
    o = sum(a)
    e = n - o
    res = 0
    c = 1
    for k in range(o + 1):
        if k % 2 == p % 2:
            res += c
        c *= o - k
        c //= k + 1
    res *= 2 ** e
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
