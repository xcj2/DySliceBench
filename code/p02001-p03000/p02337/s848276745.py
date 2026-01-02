#balls and boxes 7
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,k = map(int,readline().split())
mod = 10**9+7
def pow(n,p,mod=mod):
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod
def factrial_memo(n=10**5,mod=mod): # [1,n)までの階乗と逆元の階乗
    fact = [1, 1]  # fact[n] = (n! mod mod)
    factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod mod)
    inv = [0, 1]  # factinv 計算用
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
    return fact,factinv # warning:1-indexed list

fact,factinv = factrial_memo()

#ベル数O(k)
def bell(n,r): #nBr
    if r > n:r = n

    memo = [0]*(r+2)
    for i in range(r+1):
        if even(i):memo[i+1] = memo[i] + factinv[i]
        else:memo[i+1] = memo[i] - factinv[i]
    res = 0
    for i in range(r+1):
        res += pow(i,n)*factinv[i]*memo[r-i+1]%mod
        res %= mod
    return res

print(bell(n,k))
