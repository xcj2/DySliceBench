import math

counter = 0

def new_way(n, a, b, mod, nCa, nCb):
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] #逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル

    for i in range( 2, n + 1 ):
        g1.append( ( g1[-1] * i ) % mod )
        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )
    
    nCa = new_cmb(n, a, mod, g1, g2)
    print("a")
    nCb = new_cmb(n, b, mod, g1, g2)
    print("b")

def new_cmb(n, r, mod, g1, g2):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    ans = g1[n] * g2[r] % mod
    ans = ans * g2[n-r] % mod
    return ans


def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    bunshi = 1
    bunbo = 1
    for i in range(r):
        bunshi = bunshi * (n-i) % mod

        bunbo = bunbo * (i+1) % mod
    
    bunbo_inv = my_pow(bunbo, mod-2, mod)

    return bunshi * bunbo_inv % mod

def my_pow(x, n, mod):
    global counter
    
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x % mod
        x = x * x % mod
        n //= 2

    return K * x % mod

n, a, b = map(int,input().split())


mod = 10**9+7 #出力の制限

sum_nCr = my_pow(2, n, mod)

nCa = cmb(n, a, mod)
nCb = cmb(n, b, mod)
# nCa = 0
# nCb = 0
# new_way(n, a, b, mod, nCa, nCb)

ans = sum_nCr - (1 + nCa + nCb)
ans %= mod
print(ans)
