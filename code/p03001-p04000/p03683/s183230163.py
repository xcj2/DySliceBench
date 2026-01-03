import sys

# sys.stdin = open('a1.in')

N = 10 ** 5
M = 10 ** 9 + 7


def read_int_list():
    return list(map(int, input().split()))


def read_int():
    return int(input())


def read_str_list():
    return input().split()


def read_str():
    return input()


def solve(n, m):
    if abs(n - m) > 1:
        return 0
    res = f[m] * f[n]
    res %= M
    if m == n:
        res *= 2
        res %= M
    return res


f = [1] * (N + 1)
for i in range(1, N + 1):
    f[i] = i * f[i - 1]
    f[i] %= M

n, m = read_int_list()
res = solve(n, m)
print(res)
