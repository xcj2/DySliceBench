from sys import stdin, setrecursionlimit
from collections import Counter, deque, defaultdict
from math import floor, ceil, gcd
from bisect import bisect_left
import random
from itertools import combinations, accumulate
setrecursionlimit(100000)

INF = int(1e10)
MOD = int(1e9 + 7)

class PrimeTool(object):
    def __init__(self, n):
        self.n = n
        self.primes = []
        self.sieves = []

    def generate_primes(self):
        if len(self.primes) == 0 and len(self.sieves) == 0:
            is_prime = [True] * (self.n + 1)
            is_prime[0] = is_prime[1] = False
            self.sieves = [k for k in range(self.n + 1)]
            self.sieves[0] = 1
            for p in range(2, self.n + 1):
                if is_prime[p]:
                    self.primes.append(p)
                    for i in range(p, self.n + 1, p):
                        is_prime[i] = False
                        self.sieves[i] = p
            return self.primes

    def factorization(self, n):
        arr = []
        temp = n
        for i in range(2, int(-(-n**0.5//1))+1):
            if temp % i == 0:
                c = 0
                while temp % i==0:
                    c += 1
                    temp //= i
                arr.append((i, c))
        if temp != 1:
            arr.append((temp, 1))
        return arr

    def fast_factorization(self, num):
        # 1度計算だけ
        self.generate_primes()

        # 試し割りなしのfact
        arr = []
        temp = num
        while temp != 1:
            i = self.sieves[temp]
            c = 0
            while temp % i==0:
                c += 1
                temp //= i
            arr.append((i, c))
        if temp != 1:
            arr.append((temp, 1))
        return arr

def solve(N, A):
    tool = PrimeTool(max(A) + 1)
    primes = tool.generate_primes()
    ct = Counter()

    pair_wise = True
    for i, Ai in enumerate(A):
        arr = tool.fast_factorization(Ai)
        for p, _ in arr:
            ct[p] += 1
            if ct[p] > 1:
                pair_wise = False
                break
        if not pair_wise:
            break

    # 共通gcd
    prod = A[0]
    for k in range(1, N):
        prod = gcd(prod, A[k])
    
    if pair_wise:
        print("pairwise coprime")
    elif prod == 1:
        print("setwise coprime")
    else:
        print("not coprime")

def main():
    from builtins import int, map
    N = int(input())
    A = list(map(int, input().split()))
    solve(N, A)

if __name__ == '__main__':
    main()
