# region header
import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
import copy
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7
# endregion
# region input function


def inp():
    '''
    一つの整数
    '''
    return int(input())


def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


def str_inp():
    '''
    文字列をリストとして読み込む
    '''
    return list(input()[:-1])

# endregion


class osa_k():
    def __init__(self, n):
        """高速素因数分解

        Args:
            n (int): n以下全ての値について素因数分解できるようにする
        """
        self.n = n
        self.minFactor = list(range(0, n + 1))
        self.prime = []

    def factorize(self, i):
        if not self.prime:
            self.get_sieve_of_eratosthenes()
        factor = []
        while i != 1:
            p = self.minFactor[i]
            factor.append(p)
            i //= p
        return factor

    def get_sieve_of_eratosthenes(self):
        """エラトステネスの篩
        """
        limit = math.sqrt(self.n)
        for prime in range(2, self.n + 1):
            if prime >= limit:
                break
            if self.minFactor[prime] == prime:
                self.prime.append(prime)
                for composite in range(2 * prime, self.n + 1, prime):
                    if self.minFactor[composite] == composite:
                        self.minFactor[composite] = prime


n = inp()
a = inpl()
factorizer = osa_k(10**6)
tmp = collections.defaultdict(int)
for i in a:
    p = set(factorizer.factorize(i))
    for j in p:
        tmp[j] += 1
if not tmp.values():
    print("pairwise coprime")
    exit()
max_val = max(tmp.values())
if max_val == 1:
    print("pairwise coprime")
elif max_val == n:
    print("not coprime")
else:
    print("setwise coprime")
