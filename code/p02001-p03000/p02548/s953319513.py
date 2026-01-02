import sys
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_s = lambda: readline().rstrip().decode('utf-8')
in_nl = lambda: list(map(int, readline().split()))
in_nl2 = lambda H: [in_nl() for _ in range(H)]
in_map = lambda: [s == ord('.') for s in readline() if s != ord('\n')]
in_map2 = lambda H: [in_map() for _ in range(H)]
in_all = lambda: map(int, read().split())


class Factorize(object):

    def __init__(self, maxnum):
        self.primes = self.__smallest_prime_factors(maxnum)

    # 素因数分解 O(logN)
    def factorize(self, n):
        fct = defaultdict(lambda: 0)
        while n != 1:
            fct[self.primes[n]] += 1
            n //= self.primes[n]

        ans = 1
        for k, v in fct.items():
            ans *= (v + 1)

        return ans

    # n以下の最小の素因数を列挙する O(NlogN)
    def __smallest_prime_factors(self, n):

        prime = list(range(n + 1))

        for i in range(2, int(n**0.5) + 1):
            if prime[i] != i:
                continue
            for j in range(i * 2, n + 1, i):
                prime[j] = min(prime[j], i)
        return prime


def main():

    N = in_n()

    fct = Factorize(N + 10)

    ans = 0
    for i in range(1, N):
        ans += fct.factorize(i)

    print(ans)


if __name__ == '__main__':
    main()
