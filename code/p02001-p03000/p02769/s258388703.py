def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = 10**9 + 7  
N = 2 * 10**5 #出力の制限
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  #逆元テーブル
inverse = [0, 1]  #逆元テーブル計算用テーブル

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

def modPow(a, n, mod):
    if n == 1:
        return a
    if n % 2 == 1:
        return (a * (modPow(a, n//2, mod) ** 2)) % mod
    else:
        return (modPow(a, n//2, mod) ** 2) % mod


def modInverse(a, p):
    # calculates the modular multiplicative of a mod m.
    # (assuming p is prime).
    return modPow(a, p-2, p)


def modBinomial(n, k, p):
    # calculates C(n,k) mod p (assuming p is prime).

    numerator = 1  # n * (n-1) * ... * (n-k+1)
    for i in range(k):
        numerator = (numerator * (n-i)) % p

    denominator = 1  # k!
    for i in range(1, k+1):
        denominator = (denominator * i) % p

    # numerator / denominator mod p.
    return (numerator * modInverse(denominator, p)) % p

n, k = map(int,(input().split()))

if n <= k:
    print(modBinomial(2*n-1,n,mod))
    exit()
ans = 0
if k != 1:
    ans += 1
for i in range(1,k+1):
    ans = (ans + cmb(n,i,mod) * cmb(n-1,i,mod)) % mod

print(ans)