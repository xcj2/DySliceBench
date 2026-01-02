# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
from math import gcd
from functools import reduce
from typing import Iterable
M = 10**6
def main(N, A):
    g = reduce(gcd, A)
    if g > 1:
        print('not coprime')
        return

    s = EratosthenesSieve(M)
    u = [False] * (M + 1)
    for a in A:
        for f in set(s.factor(a)):
            if u[f]:
                print('setwise coprime')
                return
            u[f] = True
    print('pairwise coprime')

class EratosthenesSieve:
    def __init__(self, max_n: int):
        f = list(range(max_n + 1))
        for i in range(2, int(max_n**0.5) + 1):
            if f[i] < i: continue
            for j in range(i * i, max_n + 1, i):
                if f[j] == j: f[j] = i
        self.f = f

    def is_prime(self, n: int) -> bool:
        return self.f[n] == n

    def factor(self, n: int) -> Iterable[int]:
        r, f = [], self.f
        while n > 1:
            m = f[n]
            r.append(m)
            n //= m
        return r

    def primes(self) -> Iterable[int]:
        return [x for i, x in enumerate(self.f) if i == x]

if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    *A, = map(int, input().split())
    main(N, A)
