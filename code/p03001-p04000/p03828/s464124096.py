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


def is_prime(n):
    for d in range(2, n - 1):
        if n % d == 0:
            return False
    return True


def main():
    n = read_int()
    res = 1
    for p in range(2, n + 1):
        if is_prime(p):
            np = 0
            for i in range(1, n + 1):
                j = i
                while j % p == 0:
                    j //= p
                    np += 1
            res *= np + 1
            res %= M
    print(res)


main()
