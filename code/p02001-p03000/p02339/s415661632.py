import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,r = map(int,readline().split())
mod = 10**9+7

# 包除原理を用いたスターリング数
# AOJ Balls and Boxes 9で動作済み
def pow(n,p,mod=mod): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod

def factrial_memo(n=10**5,mod=mod):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
    return fact

fact = factrial_memo()

def permutation(n,r): #nPr
    return fact[n]*pow(fact[n-r],mod-2)%mod
def combination(n,r): #nCr
    return permutation(n,r)*pow(fact[r],mod-2)%mod
    #return fact[n]*pow(fact[n-r],mod-2)*pow(fact[r],mod-2)
def homogeneous(n,r): #nHr
    return combination(n+r-1,r)%mod
    #return fact[n+m-1]*pow(fact[n-1],mod-2)*pow(fact[r],mod-2)

def stirling(n,r): #nSr
    res = 0
    for i in range(r): #包除原理で「箱区別あり」を求める
        res += pow(-1,i)*combination(r,i)*pow(r-i,n)
        res %= mod
    for i in range(1,r+1): #r!で除する
        res *= pow(i,mod-2)%mod
        res %= mod
    return res

print(stirling(n,r))
