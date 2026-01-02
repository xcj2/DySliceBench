mod = 10 ** 9 + 7

# permutation: n * (n-1) * …… * (n-k+1) (mod p)
def prm(n, k, p=10**9+7):
    res = 1
    for i in range(k):
        res = res * (n-i) % p
    return res

# note: p must be a prime number
# フェルマーの小定理より
def modinv(a, p):
  return pow( a, p-2, p )
  
# combination: nPk / k! (mod p), note: p must be a prime number
def cmb(n, k, p=10**9+7):
    k = min(k, n - k)
    return prm( n, k ) * modinv( prm(k, k), p ) % p

n, a, b = map(int, input().split())

#何も選ばない1通りを除く
ans = pow(2,n,mod) - 1 - cmb(n,a) - cmb(n,b)
print(ans % mod)