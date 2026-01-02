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
    N, M = map(int, input().split())

    if N == 1:
        return print(M)

    divisors = make_divisors(M)
    divisors.sort(reverse=True)
    for r in divisors[1:]:
        if M // r < N:
            continue
        else:
            return print(r)


if __name__ == '__main__':
    main()
