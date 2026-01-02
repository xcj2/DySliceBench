s=int(input())

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# modを考慮した組み合わせ
# nCrを高速に出力
# 上の２つが必要(egcd,modinv)
def combination(n, r, mod=10**9+7):
    r = min(r, n- r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i + 1, mod) % mod
    return res




def devide_into_n_piece(n):
    remain=s-3*n
    return combination(remain+n-1, n-1)

ans=0
mod=10**9+7
for i in range(1,s//3+1):
    ans+=devide_into_n_piece(i)
    ans=ans%mod

print(ans)

