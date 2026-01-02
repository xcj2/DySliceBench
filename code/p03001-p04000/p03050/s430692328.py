import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())

    res = 0
    divisors = make_divisors(N)
    for d in divisors:
        m = d - 1
        if m > 0:
            if (N // m) == (N % m):
                res += m

    print(res)


if __name__ == '__main__':
    main()
