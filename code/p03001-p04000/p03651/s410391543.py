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


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve():
    n, k = read_int_list()
    a = read_int_list()
    if k > max(a):
        return 'IMPOSSIBLE'
    g = a[0]
    for i in range(n):
        g = gcd(g, a[i])
        if k % g == 0:
            return 'POSSIBLE'
    return 'IMPOSSIBLE'


def main():
    res = solve()
    print(res)


if __name__ == '__main__':
    main()
