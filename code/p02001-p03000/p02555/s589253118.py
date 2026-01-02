def LI():return list(map(int,input().split()))
def II():return int(input())
def yes():return print("Yes")
def no():return print("No")
INF=float("inf")
from collections import deque, defaultdict, Counter
# from heapq import heappop, heappush
# from itertools import product, combinations
# from functools import reduce, lru_cache
# from math import pi, gcd
# from decimal import Decimal

class Combination:
    """
    O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    comb = Combination(1000000)
    print(comb(5, 3))  # 10
    """
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def make_factorial_list(self, n):
        # 階乗のリストと階乗のmod逆元のリストを返す O(n)
        # self.make_modinv_list()が先に実行されている必要がある
        fac = [1]
        facinv = [1]
        for i in range(1, n+1):
            fac.append(fac[i-1] * i % self.mod)
            facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        # 0からnまでのmod逆元のリストを返す O(n)
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
        return modinv

comb=Combination(100000)
def nHk(n,k):
    return comb(n+k-1,k)%(10**9+7)
    
s=II()

q,m=s//3,s%3
# print(q,m)
mod=10**9+7
ans=0
for i in range(q,0,-1):
    j=s-i*3
    ans+=nHk(i,j)%mod
    
print(ans%mod)



