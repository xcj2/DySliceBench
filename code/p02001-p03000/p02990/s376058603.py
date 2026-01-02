import sys
from functools import reduce


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7


def cmb(N, A):
    num = reduce(lambda x, y: x * y % MOD, range(N, N - A, -1))
    den = reduce(lambda x, y: x * y % MOD, range(1, A + 1))
    # pow(den,MOD-2,MOD)はdenの逆元
    return num * pow(den, MOD - 2, MOD) % MOD


def main():
    N, K = map(int, input().split())
    R = N - K
    if R >= K - 1:
        for i in range(K):
            A = cmb(R + 1, i + 1)
            if i >= 1:
                B = cmb(K - 1, i)
            else:
                B = 1
            print(A * B % MOD)
    else:
        for i in range(R + 1):
            A = cmb(R + 1, i + 1)
            if i >= 1:
                B = cmb(K - 1, i)
            else:
                B = 1
            print(A * B % MOD)
        for i in range(K - R - 1):
            print(0)


if __name__ == "__main__":
    main()
