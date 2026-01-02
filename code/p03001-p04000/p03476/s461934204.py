"""D - 2017-like Number
"""

import math


class Sieve:
    """Sieve of Eratosthenes.

    List primes up to n.
    """

    def __init__(self, n):
        self.__prime = []
        self.__is_prime = [i >= 2 for i in range(n + 1)]

        for i in range(2, int(math.sqrt(n)) + 1):
            if self.__is_prime[i]:
                for j in range(i * i, n + 1, i):
                    self.__is_prime[j] = False

        for i in range(2, n + 1):
            if self.__is_prime[i]:
                self.__prime.append(i)

    def prime(self):
        return self.__prime

    def is_prime(self, n):
        return self.__is_prime[n]


class Fenwick:
    """Fenwick Tree implementation with 1-based index.

    Valid index: [1, N]
    """

    def __init__(self, N):
        self.fen = [0 for _ in range(N + 1)]

    def add(self, idx, val):
        while idx < len(self.fen):
            self.fen[idx] += val
            idx += idx & (-idx)

    def accum(self, idx):
        ret = 0
        while idx > 0:
            ret += self.fen[idx]
            idx -= idx & (-idx)
        return ret

    def sum(self, begin, end):
        return self.accum(end) - self.accum(begin - 1)


if __name__ == '__main__':
    Q = int(input())  # number of query
    A = [0 for _ in range(Q)]  # answer

    SIEVE = Sieve(10 ** 5)

    ACCUM = Fenwick(10 ** 5 + 1)
    for i in range(1, 10 ** 5 + 1):
        if SIEVE.is_prime(i) and SIEVE.is_prime((i + 1) // 2):
            ACCUM.add(i, 1)

    # print(ACCUM.fen)

    for i in range(Q):
        l, r = map(int, input().split())
        A[i] = ACCUM.sum(l, r)

    print('\n'.join(map(str, A)))
