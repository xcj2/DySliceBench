# 拡張ユークリッド互除法
# ax + by = gcd(a,b)の最小整数解を返す
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


# mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# nCrをすべてのr(0<=r<=n)について求める
def combination(n, mod):
    lst = [1]
    for i in range(1, n+1):
        lst.append(lst[-1] * (n+1-i) % mod * modinv(i, mod) % mod)
    return lst

H, W, A, B = map(int, input().split())
x, y = B, H-A-1
n1 = x+y
n2 = W+H-n1-2
mod = 10**9+7
C1 = combination(n1, mod)
C2 = combination(n2, mod)
ans = 0
while x<W and y>=0:
    ans += C1[x] * C2[W-x-1]
    ans %= mod
    x += 1
    y -= 1
print(ans)
