import sys

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

    er = Eratosthenes(n + 1)
    er.get_primes()
    res = 0
    for c in range(1, n + 1):
        ab = n - c
        if n - c <= 0:
            continue
        prime = er.prime_factorization(ab)
        cnt = 1
        for _, ex in prime:
            cnt *= ex + 1
        res += cnt
    print(res)



if __name__ == '__main__':
    resolve()
