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
def cal(x):
    return (x+1)/2*x
a,b = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
M = 10**9+7
L = l[::-1]
A =0
B =0
Big = BigCombination()
AA = a-1
# print(1,AA)
for i in range(a-b+1):
    k = Big.get_combination(a-i-1, b-1)
    # print(k)
    A+=k*L[i]
    B+=k*l[i]
    # print(A,B)
print((A-B)%M)
