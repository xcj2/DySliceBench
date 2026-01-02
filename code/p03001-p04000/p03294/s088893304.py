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


def bf(N, a):
    p = Sieve(max(a) + 1).prime()  # len <= 9952

    prime_to_power = {}
    for prime in p:
        prime_to_power[prime] = 0

    for i in range(N):
        ai = a[i]
        for prime in p:
            power = 0
            while ai % prime == 0:
                ai //= prime
                power += 1
            prime_to_power[prime] = max(prime_to_power[prime], power)
    lcm = 1
    for prime in prime_to_power:
        lcm *= prime ** prime_to_power[prime]
    m = lcm - 1
    ans = 0
    for ai in a:
        ans += m % ai
    return ans


def al(N, a):
    return sum(a) - len(a)


if __name__ == '__main__':
    N = int(input())  # 2 <= N <= 3000
    a = list(map(int, input().split()))  # 2 <= ai <= 100000
    # print(bf(N, a))
    print(al(N, a))