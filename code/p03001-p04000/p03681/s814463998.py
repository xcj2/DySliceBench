def input():
    import sys
    return sys.stdin.readline().rstrip()


def factorial(n, DIVISOR):
    import functools
    return functools.reduce(lambda x, y: (x % DIVISOR) * y, range(1, n + 1)) % DIVISOR


def main():
    import math
    import collections
    import itertools
    import functools

    DIVISOR = 10 ** 9 + 7
    n, m = map(int, input().split())
    if abs(n - m) > 1:
        print(0)
    elif abs(n - m) == 0:
        print((factorial(n, DIVISOR) ** 2 * 2) % DIVISOR)
    elif abs(n - m) == 1:
        print(factorial(min(n, m), DIVISOR) ** 2 * max(n, m) % DIVISOR)


if __name__ == '__main__':
    main()