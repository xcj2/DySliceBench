from collections import defaultdict
import sys
input = sys.stdin.readline


class Osak:
    def __init__(self, max_number=10 ** 6):
        self.max_number = max_number
        self.table = list(range(max_number + 1))
        self.calc_minimum_prime()

    def calc_minimum_prime(self):
        self.table[1] = 0
        for base in range(2, self.max_number + 1):
            if self.table[base] != base:
                continue
            for num in range(base, self.max_number+1, base):
                self.table[num] = base

    def judge_is_prime(self, num):
        return self.table[num] == num

    def get_factors(self, num):
        factors = set()
        while num > 1:
            prime = self.table[num]
            factors.add(prime)
            num //= prime
        return factors

    def factorize(self, num):
        factors = defaultdict(int)
        while num > 1:
            prime = self.table[num]
            factors[prime] += 1
            num //= prime
        return factors


def main():
    n = int(input())
    A = list(map(int, input().split()))

    osak = Osak(max(A))
    prime_count = defaultdict(int)
    for a in A:
        factors = osak.get_factors(a)
        for factor in factors:
            prime_count[factor] += 1
    
    if not prime_count:
        ans = 1
    else:
        ans = max(prime_count.values())

    if ans == 1:
        print("pairwise coprime")
    elif ans < n:
        print("setwise coprime")
    else:
        print("not coprime")


if __name__ == "__main__":
    main()
