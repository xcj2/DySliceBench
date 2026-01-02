import sys
from collections import defaultdict

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def prime_numbers(n):
    if n < 2:
        return []

    m = (n + 1) // 2
    p = [1] * m
    for i in range(1, int((n ** 0.5 - 1) / 2) + 1):
        if p[i]:
            p[2 * i * (i + 1) :: 2 * i + 1] = [0] * (((m - 1) - 2 * i * (i + 1)) // (2 * i + 1) + 1)

    a = [2 * i + 1 for i in range(m) if p[i]]
    a[0] = 2
    return a


def prime_factorize(n):
    a = defaultdict(int)
    primes = prime_numbers(int(n ** 0.5) + 1)
    for p in primes:
        while n % p == 0:
            a[p] += 1
            n //= p
        if n == 1:
            break
    if n != 1:
        a[n] += 1
    return a


def main():
    N = int(readline())
    a = prime_factorize(N)

    ans = 0
    for power in a.values():
        ans += int(((1 + 8 * power) ** 0.5 - 1) / 2)

    print(ans)
    return


if __name__ == '__main__':
    main()
