import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
"""
1*1*1*1*m = mなども含める
4をそのまま使う場合と2*2に分ける場合などの場合分けが必要
約数列挙からどうこうする？

"""
n,m = map(int,readline().split())
mod = 10**9+7

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
def factrial_memo(n=10**6,mod=10**9+7):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
    return fact
fact = factrial_memo()

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

prime = factrize(m)

from collections import defaultdict
dic1 = defaultdict(int)

for i in prime:
    dic1[i] += 1

ans = 1

for i in dic1.values():
    ans *= fact[n+i-1]*pow(fact[n-1],mod-2)*pow(fact[i],mod-2)
    ans %= mod
print(ans)