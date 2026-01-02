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
    q, h, s, d = read_int_list()
    n = read_int()
    res = 0
    a = n % 2
    res += min([s * a, h * 2 * a, q * 4 * a])
    a = n - a
    res += min([d * a // 2, s * a, h * 2 * a, q * 4 * a])
    return res


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
