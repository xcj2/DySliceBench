import sys

# sys.stdin = open('c1.in')

M = 10 ** 9 + 7


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def solve():
    N = 10 ** 5 + 1
    fac = [0] * N
    fac[0] = 1
    for i in range(1, N):
        fac[i] = i * fac[i - 1] % M

    n, m = read_int_list()
    if n == m:
        return 2 * fac[n] * fac[m] % M
    if abs(n - m) == 1:
        return fac[n] * fac[m] % M
    else:
        return 0


def main():
    res = solve()
    print(res)


main()
