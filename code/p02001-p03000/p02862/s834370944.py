class BigCombination(object):
    __slots__ = ["mod", "factorial", "inverse"]

    def __init__(self, mod: int = 10**9+7, max_n: int = 10**6):
        fac, inv = [1], []
        fac_append, inv_append = fac.append, inv.append

        for i in range(1, max_n+1):
            fac_append(fac[-1] * i % mod)

        inv_append(pow(fac[-1], mod-2, mod))

        for i in range(max_n, 0, -1):
            inv_append(inv[-1] * i % mod)

        self.mod, self.factorial, self.inverse = mod, fac, inv[::-1]

    def get_combination(self, n, r):
        return self.factorial[n] * self.inverse[r] * self.inverse[n-r] % self.mod

    def get_permutation(self, n, r):
        return self.factorial[n] * self.inverse[n-r] % self.mod

import math
Big = BigCombination()
n, d = map(int, input().split())
def cal(a,b):
    m = min(a,b)
    M = max(a,b)
    res = 0
    T = (m+M)//3
    if (a+b)%3 == 0 and M<=m*2:
        res = 2*M - m
        res = res// 3
        k = Big.get_combination(T, res)
        print(k)
        
    else:
        print(0)

cal(n,d)