import bisect
import heapq
import sys
import itertools
import queue


input = sys.stdin.readline
sys.setrecursionlimit(100000)
mod = 10 ** 9 + 7


class V:
    def __init__(self, f):
        self.f = f
        self.v = None

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n)

    def get(self):
        return self.v


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def P(N):
    D = []
    for n in range(1, int(N ** 0.5) + 1):
        D.append(n)
        if N // n != n:
            D.append(N // n)
    D.sort()
    return D


def main():
    N, K = read_values()
    D = P(N)
    C = [(D[i] - D[i - 1]) % mod if i != 0 else D[i] for i, d in enumerate(D)]
    dp = [0] * len(D)
    S = [D] + [[0] * len(D) for k in range(K - 1)]
    I = [bisect.bisect_left(D, N // d) for d in D]

    for k in range(1, K):
        for i in range(len(D)):
            j = I[i]
            dp[i] = (S[k - 1][j] * C[i]) % mod
            S[k][i] = (S[k][i - 1] + dp[i]) % mod
    print(S[-1][-1] % mod)


if __name__ == "__main__":
    main()
