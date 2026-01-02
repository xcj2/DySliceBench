class Sieve:
    """
    N以下の素数を列挙するエラトステネスのふるいです。
    O(NloglogN)でできます。

    Attributes
    sieveList : その数の素因数のうち最小のものの配列
    primes : N以下の素因数のリスト
    """
    def __init__(self, N):
        self.sieveList = [-1 for _ in range(N+1)]
        self.sieveList[1] = 1
        self.primes = []

        for i in range(2, N+1):
            #すでに何らかの数で割られていたらcontinue
            if self.sieveList[i] != -1:
                continue
            self.primes.append(i)
            for j in range(i, N+1, i):
                if self.sieveList[j] != -1:
                    continue
                self.sieveList[j] = i

    def getPrimes(self):
        return self.primes

    def getSieveList(self):
        return self.sieveList

class FastFactorization(Sieve):
    """
    高速素因数分解です。
    与えられたL個の数がA以下の時、
    エラトステネスでO(AloglogA)＋素因数分解でO(LlogA) = O(AloglogA+NlogA)でできます。
    """

    def __init__(self, N):
        """
        前処理でスーパークラスのエラトステネスを使ってN以下の素因数を列挙します。
        """
        super().__init__(N)
        self.N = N
        self.sieveList = self.getSieveList()

    def factorize(self, x):
        if x > self.N:
            raise ValueError("与えられた数がエラトステネスのリストの上限を超えている")
        p = set()
        # p = []
        while x > 1:
            divisor = self.sieveList[x]
            x //= divisor
            p.add(divisor)
            # p.append(divisor)
        return p

import math
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

#is setwise?
gcd = A[0]
for i in range(1, N):
    gcd = math.gcd(gcd, A[i])
isSetwise = (gcd == 1)

#is pairwise?
maxNum = max(A)
factorizor = FastFactorization(maxNum)
factors = defaultdict(int)
isPairwise = True
for i in range(N):
    p = factorizor.factorize(A[i])
    for x in p:
        if factors[x]:
            isPairwise = False
            break
        else:
            factors[x] = 1

if isPairwise:
    print("pairwise coprime")
elif isSetwise:
    print("setwise coprime")
else:
    print("not coprime")
