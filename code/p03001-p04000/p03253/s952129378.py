import math
import copy
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
from bisect import bisect_left, bisect_right
# import numpy as np

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W

# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def i_inpl(): return int(input())
def s_inpl(): return map(int,input().split())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")
MAX_DIGIT = 50

############
############
############
class Prime:
    seed_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def is_prime(self, n):
        """
        prime test (hybrid)

        :param n:
        :return: boolean
        """
        is_prime_common = self.is_prime_common(n)
        if is_prime_common is not None:
            return is_prime_common

        if n < 2000000:
            return self.is_prime_brute_force(n)
        else:
            return self.is_prime_miller_rabin(n)

    def is_prime_common(self, n):
        if n == 1: return False
        if n in Prime.seed_primes: return True
        if any(map(lambda x: n % x == 0, self.seed_primes)): return False

    def is_prime_brute_force(self, n):
        for k in range(2, int(math.sqrt(n)) + 1):
            if n % k == 0:
                return False
        return True

    def is_prime_miller_rabin(self, n):
        d = n - 1
        while d & 1 == 0:
            d >>= 1

        witnesses = self.get_witnesses(n)

        for w in witnesses:
            y = pow(w, d, n)

            while d != n - 1 and y != 1 and y != n - 1:
                y = (y * y) % n
                d <<= 1

            if y != n - 1 and d & 1 == 0:
                return False

        return True

    def get_witnesses(self, num):
        def _get_range(num):
            if num < 2047:
                return 1
            if num < 1373653:
                return 2
            if num < 25326001:
                return 3
            if num < 3215031751:
                return 4
            if num < 2152302898747:
                return 5
            if num < 3474749660383:
                return 6
            if num < 341550071728321:
                return 7
            if num < 3825123056546413051:
                return 9
            return 12

        return self.seed_primes[:_get_range(num)]

    def gcd(self, a, b):
        if a < b:
            return self.gcd(b, a)
        if b == 0:
            return a
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def f(x, n, seed):
        p = Prime.seed_primes[seed % len(Prime.seed_primes)]
        return (p * x + seed) % n

    def find_factor(self, n, seed=1):
        if self.is_prime(n):
            return n

        x, y, d = 2, 2, 1
        count = 0
        while d == 1:
            count += 1
            x = self.f(x, n, seed)
            y = self.f(self.f(y, n, seed), n, seed)
            d = self.gcd(abs(x - y), n)

        if d == n:
            return self.find_factor(n, seed+1)
        return self.find_factor(d)

    def find_factors(self, n):
        primes = {}
        if self.is_prime(n):
            primes[n] = 1
            return primes

        while n > 1:
            factor = self.find_factor(n)

            primes.setdefault(factor, 0)
            primes[factor] += 1

            n //= factor

        return primes


prime = Prime()

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N, M = l_inpl()
ans = 1
for i, k in prime.find_factors(M).items():
    ans *= cmb(k + N - 1, k) 
    ans %= (int(10e8) + 7)

print(ans % (int(10e8) + 7))
