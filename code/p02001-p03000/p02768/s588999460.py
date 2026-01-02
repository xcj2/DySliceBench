import sys

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def modInverse(a, p):
    return pow(a, p - 2, p)


def modBinomial(n, k, p):
    numerator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % p

    denominator = 1
    for i in range(1, k + 1):
        denominator = (denominator * i) % p

    return (numerator * modInverse(denominator, p)) % p


def main():
    N, A, B = [int(x) for x in input().split()]

    MOD = 10 ** 9 + 7

    ans = pow(2, N - 1, MOD)
    ans = ans * 2
    a = modBinomial(N, A, MOD)
    b = modBinomial(N, B, MOD)
    print((ans - a - b) % MOD - 1)


if __name__ == '__main__':
    main()
