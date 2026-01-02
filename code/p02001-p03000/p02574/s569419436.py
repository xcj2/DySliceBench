import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


class Eratosthenes:
    def __init__(self, n):
        self.n = n
        self.min_factor = [-1] * (n + 1)
        self.min_factor[0], self.min_factor[1] = 0, 1

    def get_primes(self):
        primes = []
        is_prime = [True] * (self.n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, self.n + 1):
            if not is_prime[i]:
                continue
            primes.append(i)
            self.min_factor[i] = i
            for j in range(i * 2, self.n + 1, i):
                is_prime[j] = False
                if self.min_factor[j] == -1:
                    self.min_factor[j] = i
        return primes

    def prime_factorization(self, n):
        res = []
        while n != 1:
            prime = self.min_factor[n]
            exp = 0
            while self.min_factor[n] == prime:
                exp += 1
                n //= prime
            res.append([prime, exp])
        return res


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    MAX = max(A)
    tot_gcd = A[0]
    for a in A:
        tot_gcd = gcd(tot_gcd, a)

    if tot_gcd != 1:
        print("not coprime")
    else:
        er = Eratosthenes(MAX)
        er.get_primes()
        check = [False] * (MAX + 1)
        for a in A:
            for p, _ in er.prime_factorization(a):
                if not check[p]:
                    check[p] = True
                else:
                    print("setwise coprime")
                    exit()
        print("pairwise coprime")


if __name__ == '__main__':
    resolve()
