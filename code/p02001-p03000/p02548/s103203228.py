from collections import defaultdict
N = int(input())

fact = [1] * (10**3+1)
for i in range(2, 10**3+1):
    fact[i] = i * fact[i-1]

def nCr(n, r):
    return fact[n] // (fact[r] * fact[n-r])

class Sieve:
    """
    N以下の素数を列挙するエラトステネスのふるいです。
    O(NloglogN)でできます。

    Attributes
    sieveList : その数の素因数のうち最小のものの配列
    primes : N以下の素数のリスト
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
    与えられたL個の数がすべてA以下の時、
    エラトステネスでO(AloglogA)＋素因数分解でO(LlogA) = O(AloglogA+LlogA)でできます。
    「試し割り」をする必要が無いのではやいです。
    """

    def __init__(self, N):
        """
        前処理でスーパークラスのエラトステネスを使ってN以下の素因数を列挙します。
        """
        super().__init__(N)
        self.N = N
        self.sieveList = self.getSieveList()
        self.factorSet = None
        self.factorDict = None

    def factorize(self, x):
        if x > self.N:
            raise ValueError("与えられた数がエラトステネスのリストの上限を超えている")
        factorDict = defaultdict(int)
        while x > 1:
            divisor = self.sieveList[x]
            x //= divisor
            # factors += 1
            factorDict[divisor] += 1

        self.factorDict = factorDict

    def getFactorSet(self):
        return self.factorSet

    def getFactorDict(self):
        return self.factorDict


ff = FastFactorization(N+1)
ans = 0
for c in range(1, N):
    num = N - c
    # print(num, ff.factorize(num))
    tmp = 1
    if num == 1:
        ans += 1
    else:
        ff.factorize(num)
        factors = ff.getFactorDict()
        for v in factors.values():
            tmp *= nCr(2 + v - 1, v)
        ans += tmp

print(ans)
