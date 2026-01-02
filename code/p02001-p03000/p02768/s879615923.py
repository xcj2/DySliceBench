# 乗法のmod逆元 (mod-2乗)
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)
 
# nCr mod m
# modinvが必要
# rがn/2に近いと非常に重くなる
def comb(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res
  
def binary(n):
    return bin(n)[2:]

# バイナリ法
def pow_by_binary(a, x, n): # a^x mod n
    x = [int(b) for b in binary(x)]
    y = a
    for i in range(1, len(x)):
        y = (y**2) % n
        if x[i] == 1:
            y = (y * a) % n
    return y
  
n,a,b = [int(i) for i in input().split()]
mod = 10**9+7
ans = pow_by_binary(2,n,mod)-1-comb(n,a,mod)-comb(n,b,mod)
if ans < 0:
  ans += mod
print(ans%mod)