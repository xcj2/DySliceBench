import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def ii(): return int(input())
def mi(): return map(int, input().rstrip().split())
def lmi(): return list(map(int, input().rstrip().split()))
def li(): return list(input().rstrip())
# template


# BEGIN CUT HERE
MOD = 10**9 + 7


class Modint():
    '''
        自動でMODで割った余りを返してくれる。
    '''

    def __init__(self, n, mod=MOD):
        if n >= 0:
            self.n = n % mod
        else:
            self.n = (mod - (-n) % mod) % mod
        self.mod = mod

    def __eq__(self, other):
        return self.n == int(other)

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        return Modint(-self.n, self.mod)

    def __str__(self):
        return str(self.n)

    def __int__(self):
        return int(self.n)

    def __iadd__(self, other):
        self.n += int(other)
        self.n %= self.mod
        return self

    def __radd__(self, other):
        self.n += int(other)
        self.n %= self.mod
        return self

    def __isub__(self, other):
        self.n -= int(other)
        self.n %= self.mod
        return self

    def __rsub__(self, other):
        self.n -= int(other)
        self.n %= self.mod
        return self

    def __imul__(self, other):
        self.n = self.n * int(other) % self.mod
        return self

    def __rmul__(self, other):
        self.n = self.n * int(other) % self.mod
        return self

    def inverse(self):
        return self.__class__(pow(self.n, self.mod - 2, self.mod), self.mod)

    def __ifloordiv__(self, other):
        self *= pow(int(other), self.mod - 2, self.mod)
        return self

    def __rfloordiv__(self, other):
        self *= pow(int(other), self.mod - 2, self.mod)
        return self

    def __add__(self, other):
        self += other
        return self

    def __sub__(self, other):
        self -= other
        return self

    def __mul__(self, other):
        self *= other
        return self

    def __floordiv__(self, other):
        self //= other
        return self

    # '''コンビネーション絡みの定義
    #     ･ comb(n,k):特に前処理をせずnCkを求める
    # '''

    # def comb(self, n, k):
    #     if n < k or k < 0:
    #         return Modint(0)
    #     res = Modint(1)
    #     for i in range(int(k)):
    #         res *= Modint(n - i)
    #         res //= Modint(i + 1)
    #     return res

    # def H(self, n, k):
    #     if n < 0 or k < 0:
    #         return Modint(0)
    #     elif n == 0 and k == 0:
    #         return Modint(1)
    #     else:
    #         return self.comb(n + k - 1, n)


class Combination():
    def __init__(self, sz):
        self.fact = [0] * (sz + 1)
        self.rfact = [0] * (sz + 1)
        self.fact[0] = 1
        self.rfact[sz] = 1
        for i in range(1, sz + 1):
            self.fact[i] = int(self.fact[i - 1] * Modint(i))
        self.rfact[sz] = int(Modint(self.fact[sz]).inverse())
        for i in range(sz - 1, -1, -1):
            self.rfact[i] = int(self.rfact[i + 1] * Modint(i + 1))

    def fact(self, k):
        return self.fact[k]

    def rfact(self, k):
        return self.rfact[k]

    def P(self, n, k):
        if k < 0 or n < k:
            return 0
        return self.fact[n] * self.rfact[n - k]

    def C(self, n, k):
        if k < 0 or n < k:
            return 0
        return self.fact[n] * self.rfact[k] * self.rfact[n - k]

    def H(self, n, k):
        if n < 0 or k < 0:
            return 0
        elif k == 0:
            return 1
        return self.C(n + k - 1, n)


if __name__ == '__main__':
    N, K = mi()
    res = Combination(N)
    for i in range(1, K + 1):
        print(res.C(K - 1, i - 1) * res.H(N - K - i + 1, i + 1) % MOD)
