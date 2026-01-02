import sys
readline = sys.stdin.buffer.readline
from collections import Counter
n,m = map(int,readline().split())
mod = 10**9+7

"""素因数分解"""
def factrize(n):
    b = 2
    fct = []
    while b*b <= n:
        while n % b == 0:
            n //= b
            #もし素因数を重複させたくないならここを加えてfct.append(b)を消す
            """
            if not b in fct:
                fct.append(b)
            """
            fct.append(b)
        b = b+1
    if n > 1:
        fct.append(n)
    return fct #リストが帰る
def pow(n,p,mod=10**9+7): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod
def factrial_memo(n=20**5+1,mod=10**9+7):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
    return fact
fact = factrial_memo()
def fermat_cmb(n, r, mod=10**9+7): #needs pow,factrial_memo(only fact). return nCk
    return fact[n] * pow(fact[r],mod-2) * pow(fact[n-r],mod-2) %mod

lst1 = factrize(m)

c = Counter(lst1)

ans = 1
for i in c.values():
    ans *= fermat_cmb(n+i-1,i)
    ans %= mod

print(ans)
    