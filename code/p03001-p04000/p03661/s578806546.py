import sys

# sys.stdin = open('c1.in')


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
    res = 2 * 10 ** 10
    x = 0
    y = sum(a)
    for i in range(n - 1):
        x += a[i]
        y -= a[i]
        d = abs(x-y)
        if res > d:
            res = d
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
