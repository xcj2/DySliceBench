import math


def divisors(n, sort=False):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    if sort:
        divisors.sort()
    return divisors


def main():
    N = int(input())

    def is_ok(n, d):
        while True:
            if n % d == 0:
                n = n / d
            else:
                return n % d == 1

    count = len(divisors(N - 1)) - 1

    for div in divisors(N):
        if div == 1:
            continue
        if is_ok(N, div):
            count += 1

    print(count)


if __name__ == '__main__':
    main()
