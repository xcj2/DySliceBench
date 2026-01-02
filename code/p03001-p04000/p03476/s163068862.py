from sys import stdin, setrecursionlimit
from itertools import accumulate

setrecursionlimit(10 ** 9)
INF = 1 << 60


def input():
    return stdin.readline().strip()


def prime_numbers(n):
    if n < 2:
        return []

    m = (n + 1) // 2
    p = [True] * m
    for i in range(1, int((n ** 0.5 - 1) / 2) + 1):
        if p[i]:
            for j in range(2 * i * (i + 1), m, 2 * i + 1):
                p[j] = False

    return {2} | {2 * i + 1 for i in range(1, m) if p[i]}

def main():
    N = 10 ** 5
    primes = prime_numbers(N)
    a = [1 if n in primes and (n + 1) // 2 in primes else 0 for n in range(N + 1)]
    a = tuple(accumulate(a))

    ans = []
    Q, *LR = map(int, open(0).read().split())
    for l, r in zip(*[iter(LR)] * 2):
        ans.append(a[r] - a[l - 1])

    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    main()