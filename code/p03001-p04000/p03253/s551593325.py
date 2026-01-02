"""
8:30:00
"""

from collections import defaultdict
def getprime(n):
    if not isinstance(n, int):
        raise TypeError("Input int")
    if n < 2:
        raise ValueError("N >= 2")
    prime = []
    # 約数はsqrt(N)まで調べればOK
    data = [i+1 for i in range(1,n)]
    while True:
        p = data[0]
        if p >= int(n**0.5):
            return prime+data
        prime.append(p)
        # pで割り切れないものだけを残す
        data = [d for d in data if d%p != 0]

def factorization(n):
    factors = defaultdict(int)
    primes = getprime(int(n**0.5))
    for prime in primes:
        while n % prime == 0:
            factors[prime] += 1
            n //= prime
            # print(factors,n)
    if n != 1:
        factors[n] += 1
    return factors


def modconb(n,k,mod):
    # テーブルを作る
    fac = [0]*(n+1)
    finv = [0]*(n+1)
    inv = [0]*(n+1)  

    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,n+1):
        fac[i] = fac[i-1]*i % mod
        inv[i] = mod - inv[mod%i] * (mod//i) % mod
        finv[i] = finv[i-1] * inv[i] % mod

    if n<k: return 0
    if n<0 or k<0: return 0
    return(fac[n]*(finv[k]*finv[n-k]%mod)%mod)

"""
1 * 1 * 1のどこに素因数をかけるか
3^3だとして
どこかで3回3をかけないといけない
a + b + c = 3 //重複組合せ
3*3-1C3
こいつをかけ合わせると答えになる
modconbいる
"""

mod = 10**9 + 7
n, m = map(int, input().split())
if m == 1:
    print(1)
    exit()
factors = factorization(m)
ans = 1
for k in factors.keys():
    x = factors[k]
    ans *= modconb(x+n-1,x,mod)
    ans %= mod
print(ans)
